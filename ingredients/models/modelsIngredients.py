from django.db import models
from django.contrib.auth.models import User


class FoodGroups(models.Model):
    group = models.CharField(max_length=500)

    def __str__(self):
        return str(self.group)


class Ingredients (models.Model):
    # group = models.CharField(max_length=500)
    food_name = models.CharField(max_length=500)
    foodgroup = models.ForeignKey(FoodGroups, on_delete=models.CASCADE, null=True, related_name='ingredients')

    def __str__(self):
        return str(self.food_name)



