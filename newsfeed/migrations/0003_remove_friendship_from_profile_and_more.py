# Generated by Django 4.2 on 2023-05-19 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsfeed', '0002_alter_post_user_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendship',
            name='from_profile',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='to_profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='react',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Follower',
        ),
        migrations.DeleteModel(
            name='Friendship',
        ),
        migrations.DeleteModel(
            name='Hobby',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
