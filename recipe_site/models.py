from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Recipes(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    #telling django how to the find the url to any specific instance of a post
    #pk > primary key, self.pk is the primary key of the instance. We used this in the url for the detailed post
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})