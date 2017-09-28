from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User)
    description = models.TextField()
    # pricing = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'User profile {}'.format(self.user.get_full_name)