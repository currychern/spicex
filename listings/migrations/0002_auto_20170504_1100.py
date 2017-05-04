# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_duration',
            field=models.PositiveSmallIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='listing',
            name='pickup_location',
            field=models.CharField(default='Austin, TX', max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='pickup_time',
            field=models.TextField(default='Wednesday May 24, 2017 from 5:00-8:00PM'),
        ),
    ]