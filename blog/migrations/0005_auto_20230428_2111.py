# Generated by Django 3.2.17 on 2023-04-28 21:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_alter_posts_preview'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Story',
        ),
        migrations.RenameModel(
            old_name='Thoughts',
            new_name='Thought',
        ),
    ]
