from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .models import SessionsIndividual, Booking, Profile, User
from .forms import BookingsForm, ProfileForm


class CreateIndividualSessions(View):
    def get(self, request, *args, **kwargs):
        """
        Show List Of All Possible Sessions
        """
        sessions = SessionsIndividual.objects.all()
        context = {
            'sessions': sessions
        }

        return render(request, "bookings/sessions_list.html", context)


@login_required(redirect_field_name='/accounts/login')
def book_session(request):
    """
    Make A Booking
    Login required
    """
    options = SessionsIndividual.objects.all()
    booking_form = BookingsForm(request.POST or None)
    if request.method == "POST":
        if booking_form.is_valid():
            # Finds corresponding sessions in SessionsIndividual
            # and sets its value to True
            for session in options:
                if booking_form.instance.session == session:
                    x = session
                    x.booked = True
                    x.save()
            booking_form.instance.name = request.user
            booking_form.save()
            return render(
                    request, 'bookings/confirm_booking.html', {
                        "name": request.user, "session": x
                    })
    template = "bookings/bookings_list.html"
    context = {
        "form": booking_form,
    }
    return render(request, template, context)


@login_required(redirect_field_name='/accounts/login')
def user_bookings_session(request):
    """
    User Bookings Display
    Login required
    """
    # Filter so user can only see their own bookings
    user_bookings = Booking.objects.filter(name=request.user.id).all()
    context = {
        "bookings": user_bookings
    }
    return render(request, "bookings/user_bookings.html", context)


def cancel_booking(request, booking_id):
    """
    User Cancel Booking Button
    """
    booking_to_delete = get_object_or_404(Booking, id=booking_id)
    # Find corresponding session and update "booked" status to False
    sessions = SessionsIndividual.objects.all()
    for session in sessions:
        if session == booking_to_delete.session:
            x = session
            x.booked = False
            x.save()
    booking_to_delete.delete()
    return redirect("user_bookings")


@login_required(redirect_field_name='/accounts/login')
def user_profile_update(request):
    """
    User Profile Update
    Login required
    """
    print("Creating/updating profile")
    profile = Profile.objects.filter(name=request.user.id).first()
    print(profile)
    profile_form = ProfileForm(request.POST or None, instance=profile)
    if request.method == "POST":
        if profile_form.is_valid():
            profile_form.instance.user = request.user
            profile_form.instance.name_id = request.user.id
            profile_form.instance.profile_ready = True
            profile_form.save()
        return redirect("user_profile")
    template = "bookings/user_profile_update.html"
    context = {
        "form": profile_form,
    }
    return render(request, template, context)


@login_required(redirect_field_name='/accounts/login')
def user_profile(request):
    """
    User Profile Display page
    Login required
    """
    profile = Profile.objects.filter(name=request.user.id).all()
    profile_values = profile.values()
    user_bookings = Booking.objects.filter(name=request.user.id).all()
    return render(request, 'bookings/user_profile.html', {
        "profile": profile,
        "profile_values": profile_values,
        "bookings": user_bookings
        })


@login_required(redirect_field_name='/accounts/login')
def delete_profile(request):
    """
    User Delete Profile Button
    Login required
    """
    profile_to_delete = Profile.objects.filter(name=request.user.id).all()
    profile_to_delete.delete()

    return redirect("user_profile")
