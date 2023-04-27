from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Posts, Thoughts
from .forms import CommentForm


class PostOverview(generic.ListView):
    queryset = Posts.objects.filter(status=1).order_by("-created_on")
    template_name = "posts_overview.html"
    paginate_by = 2
    model = Posts

    def get(self, request, *args, **kwargs):
        """
        This view renders the blog page and also all published posts
        """
        posts = Posts.objects.all()
        paginator = Paginator(posts, 2)
        page = request.GET.get('page')
        page_post = paginator.get_page(page)

        return render(
            request, 'blog/posts_overview.html',
            {'posts': posts, 'page_post': page_post}
            )


class SinglePost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Posts.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/single_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Posts.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request,
                             'Your comment has been submitted,'
                             'it will display once approved.')
        else:
            comment_form = CommentForm()
            messages.error(request, 'Please try again')

        return render(
            request,
            "blog/single_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Posts, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('single_post', args=[slug]))
