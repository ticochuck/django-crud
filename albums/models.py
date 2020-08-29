from django.db import models
from django.urls import reverse

# Create your models here.

class Records(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    artist = models.CharField(max_length=64)
    description = models.TextField()


    def __str__(self):
        return f'{self.title}, {self.artist}'


    def get_absolute_url(self):
        return reverse('home')