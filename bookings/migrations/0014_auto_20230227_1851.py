# Generated by Django 3.2.17 on 2023-02-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0013_alter_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Guest', max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
