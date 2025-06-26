from django.db import models
from django.contrib.auth.models import AbstractUser

class Movie(models.Model):
    name=models.CharField(max_length=100)
    rating=models.DecimalField(decimal_places=1,max_digits=2)
    genre=models.CharField(max_length=100)
    language=models.CharField(max_length=100)
    re_year=models.DateField(null=True)


class CustomUser(AbstractUser):
    confirm=models.CharField(max_length=100)