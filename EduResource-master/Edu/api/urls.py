from django.urls import path
from .views import NearbySearchView, place_details

urlpatterns = [
    path('nearby-search/', NearbySearchView.as_view(), name='nearby-search'),
    path('place-details/', place_details, name='place-details')


]