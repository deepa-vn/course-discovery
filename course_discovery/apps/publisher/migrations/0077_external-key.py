# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-06 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0076_publisher_masters_track_rerun'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserun',
            name='external_key',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='historicalcourserun',
            name='external_key',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
