# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Listing
from .forms import ListingForm

def listings(request):
    listings = Listing.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'listings/listings.html', {'listings': listings})

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

def listing_new(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.author = request.user
            listing.published_date = timezone.now()
            listing.save()
            return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_edit.html', {'form': form})

def listing_edit(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.author = request.user
            listing.published_date = timezone.now()
            listing.save()
            return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_edit.html', {'form': form})

def listing_remove(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    listing.delete()
    return redirect('listings')
