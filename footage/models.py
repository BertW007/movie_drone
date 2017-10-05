from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


VIDEO_TYPES = [
    ('video', "video"),
    ('photography', "photography"),
    ('video and photography', "video and photography"),
]

CITY = [

    ("Białystok"  ,"Białystok"  ),
    ("Bydgoszcz"  ,"Bydgoszcz"  ),
    ("Częstochowa","Częstochowa"),
    ("Gdynia"     ,"Gdynia"     ),
    ("Gdańsk"     ,"Gdańsk"     ),
    ("Łódź"       ,"Łódź"       ),
    ("Katowice"   ,"Katowice"   ),
    ("Kraków"     ,"Kraków"     ),
    ("Lublin"     ,"Lublin"     ),
    ("Opole"      ,"Opole"      ),
    ("Poznań"     ,"Poznań"     ),
    ("Radom"      ,"Radom"      ),
    ("Sosnowiec"  ,"Sosnowiec"  ),
    ("Szczecin"   ,"Szczecin"   ),
    ("Toruń"      ,"Toruń"      ),
    ("Warszawa"   ,"Warszawa"   ),
    ("Wrocław"    ,"Wrocław"    ),

]


class Footage(models.Model):
    link = models.URLField()
    author = models.ForeignKey(User)
    description = models.TextField()

    def __str__(self):
        return self.description

    def get_delete_url(self):
        return reverse('delete-footage', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('console', kwargs={'pk': self.author.pk})



class FootageDetail(models.Model):
    person = models.OneToOneField(User)
    about_me = models.TextField()
    pricing = models.DecimalField(max_digits=6, decimal_places=2)
    video_type = models.CharField(choices=VIDEO_TYPES, max_length=100)
    city = models.CharField(choices=CITY, max_length=64)

    def __str__(self):
        return 'User {}, about me: {}'.format(self.person.get_username(), self.about_me)

    # def get_absolute_url(self):
    #     return reverse('console', kwargs={'pk': self.person.pk})