# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage', '0005_remove_user_avatar'),
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulletin',
            name='follower',
        ),
        migrations.AddField(
            model_name='bulletin',
            name='follower',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bulletin_follower', to='user_manage.User'),
        ),
    ]
