from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = (
            'title',
            'description',
            'type',
            'pickup_location',
            'pickup_time',
            'list_duration',
        )
