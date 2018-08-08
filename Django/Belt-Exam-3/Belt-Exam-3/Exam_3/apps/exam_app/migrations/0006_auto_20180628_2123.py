# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-29 01:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0005_auto_20180628_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='users',
        ),
        migrations.AddField(
            model_name='list',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='exam_app.User'),
            preserve_default=False,
        ),
    ]
