# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 05:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_manager', '0002_auto_20171103_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_manager.Team'),
        ),
    ]
