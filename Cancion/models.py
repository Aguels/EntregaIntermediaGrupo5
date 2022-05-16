from django.db import models

class Song(models.Model):
    nombre = models.CharField(max_length=200)
    letra = models.TextField()
    link = models.URLField()
    acordes = models.CharField(max_length=200)
    tono = models.CharField(max_length=3)
    def __str__(self):
        return f"{self.nombre}"

