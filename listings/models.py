# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Listing(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=100)
    pickup_location = models.CharField(
        max_length=200, default='Austin, TX')
    pickup_time = models.TextField(
        default='Wednesday May 24, 2017 from 5:00-8:00PM'
    )
    list_duration = models.PositiveSmallIntegerField(
        default=5)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
