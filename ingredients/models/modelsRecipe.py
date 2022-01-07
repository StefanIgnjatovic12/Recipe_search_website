from django.db import models
class DisplayRecipe (models.Model):
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

class FavoriteRecipe (models.Model):
    # make it so that it inherits from display recipe instead of this garbage
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