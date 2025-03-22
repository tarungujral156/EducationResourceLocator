from django.contrib import admin
from .models import Resource, Event

# Register your models here.

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ["name","type","location","timings","ratings"]
    search_fields = ["name","type","location"]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["name","date","description","organizer_contact"]
    search_fields = ["name","date","organizer_contact"]