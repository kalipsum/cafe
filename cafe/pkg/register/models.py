from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=400)
    key_expires = models.DateTimeField()


class UserInfo(models.Model):
    username = models.CharField(max_length=70)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=70)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=10)
    flat = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)


