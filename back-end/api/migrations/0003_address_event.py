# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20161006_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('z_code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('location', models.CharField(max_length=40)),
                ('notes', models.TextField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Address')),
            ],
        ),
    ]
