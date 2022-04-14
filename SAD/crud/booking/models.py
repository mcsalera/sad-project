from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_listed = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('listing-detail', kwargs={'pk': self.pk})
    