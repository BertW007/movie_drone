from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Footage(models.Model):
    link = models.URLField()
    author = models.ForeignKey(User)
    description = models.TextField


class UserDetails(models.Model):
    person = models.OneToOneField(User)
    about_me = models.TextField()
    pricing = models.DecimalField(max_digits=6, decimal_places=2)
    video_type = models.CharField(choices=VIDEO_TYPES, max_length=100)
    cities = models.ManyToManyField(City)

    def __str__(self):
        return self.about_me

    def get_absolute_url(self):
        return reverse('console', kwargs={'pk': self.person.pk})


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

VIDEO_TYPES = [
    ('video', "video"),
    ('photography', "photography"),
    ('video and photography', "video and photography"),
]