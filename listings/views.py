# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Listing

def listings(request):
    listings = Listing.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'listings/list.html', {'listings': listings})

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listings/listing_detail.html', {'listing': listing})
