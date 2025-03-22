from django.db import models

# Create your models here.

class Resource(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    timings = models.CharField(max_length=255,blank=True,null=True)
    ratings = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()
    organizer_contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name