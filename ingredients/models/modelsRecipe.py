from django.db import models
from django.contrib.auth.models import User

class FavoriteRecipe (models.Model):
    title = models.TextField(max_length=500)
    ingredients = models.TextField(max_length=500)
    link = models.URLField()
    img = models.URLField()
    calories = models.TextField(max_length=500)
    fat = models.TextField(max_length=500)
    carbs = models.TextField(max_length=500)
    protein = models.TextField(max_length=500)
    cholesterol = models.TextField(max_length=500)
    sodium = models.TextField(max_length=500)
    saturated_fat = models.TextField(max_length=500)
    sugar = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.title)