from django.db import models
from django.utils import timezone

class Event(models.Model):

    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    start_data = models.DateField(_null= True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    img_url = models.URLField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    twitter_url = models.URLField(blank=True)
    primal_url = models.URLField(blank=True)

    def is_expired(self):
        return self.start_data and self.start_data < timezone.now()
    
    def __str__(self):
        return self.name
    

class Community(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    desc = models.TextField(blank=True)
    location = models.CharField(max_length=250, blank=True)
    twitter_url = models.URLField(blank=True)
    primal_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    img_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
    

class CircularEconomy(models.Model):
    name = models.CharField(max_length=250)
    slug =  models.SlugField(unique=True)
    desc = models.TextField(blank=True)
    locations = models.CharField(blank=True)
    twitter_url = models.URLField(blank=True)
    primal_url = models.URLField(blank=True)
    img_url = models.URLField(blank=True)

    def __str__(self):
        return self.name