# Generated by Django 4.0.3 on 2022-05-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_avatar_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/profile_images'),
        ),
    ]
