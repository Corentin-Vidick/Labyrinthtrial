# Generated by Django 3.2.17 on 2023-04-28 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_posts_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='preview',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
