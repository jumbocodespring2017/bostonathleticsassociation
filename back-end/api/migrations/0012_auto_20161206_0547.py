# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 05:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_merge_20161201_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_Captain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_object', to='api.Event')),
                ('user_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_object', to=settings.AUTH_USER_MODEL)),
                ('volunteer_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_object', to='api.Volunteer')),
            ],
        ),
        migrations.AlterField(
            model_name='attendee',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
