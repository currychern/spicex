from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listings, name='listings'),
    url(r'^listing/(?P<pk>\d+)/$', views.listing_detail, name='listing_detail'),
]
