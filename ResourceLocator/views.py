from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Resource, Event
from .serializers import ResourceSerializer, EventSerializer

class ResourceViewSet(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

def index(request):
    return render(request, "index.html")

def map_view(request):
    return render(request, "map.html")