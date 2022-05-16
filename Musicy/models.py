from django.contrib.auth.models import User
from django.db import models

class Pic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="images",null=True,blank=True)