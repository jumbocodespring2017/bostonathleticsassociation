# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20161019_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='duration',
        ), 
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
