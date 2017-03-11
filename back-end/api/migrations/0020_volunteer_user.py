# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 00:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0019_auto_20170306_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
