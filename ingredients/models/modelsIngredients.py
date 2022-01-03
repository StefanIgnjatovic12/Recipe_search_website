from django.db import models
from django.contrib.auth.models import User


class Ingredients (models.Model):
    group = models.CharField(max_length=500)
    food_name = models.CharField(max_length=500)
    selection = models.ManyToManyField(User, related_name='selection', default=None, blank=True)
    selection_count = models.BigIntegerField(default='0')

    def __str__(self):
        return str(self.food_name)

