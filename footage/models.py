from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


VIDEO_TYPES = [
    ('video', "video"),
    ('photography', "photography"),
    ('video and photography', "video and photography"),
]


class Footage(models.Model):
    link = models.URLField()
    author = models.ForeignKey(User)
    description = models.TextField

    def __str__(self):
        return self.link

    def get_delete_url(self):
        return reverse('delete-footage', kwargs={'pk': self.pk})


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FootageDetail(models.Model):
    person = models.OneToOneField(User)
    about_me = models.TextField()
    pricing = models.DecimalField(max_digits=6, decimal_places=2)
    video_type = models.CharField(choices=VIDEO_TYPES, max_length=100)
    city = models.ManyToManyField(City)

    def __str__(self):
        return self.about_me

    # def get_absolute_url(self):
    #     return reverse('console', kwargs={'pk': self.person.pk})
