# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-16 10:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iclone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='user_from',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='user_to',
        ),
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='who_following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
