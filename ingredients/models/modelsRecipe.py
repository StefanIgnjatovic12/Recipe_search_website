from django.db import models
from django.contrib.auth.models import User

class FavoriteRecipe (models.Model):
    title = models.TextField(max_length=500)
    used_ingredients = models.JSONField(blank=True, null=True)
    missed_ingredients = models.JSONField(blank=True, null=True)
    used_ingredient_count = models.IntegerField(blank=True, null=True)
    missed_ingredient_count = models.IntegerField(blank=True, null=True)
    servings = models.IntegerField(blank=True, null=True)
    ready_in = models.IntegerField(blank=True, null=True)
    cuisines = models.JSONField(blank=True, null=True)
    link = models.URLField()
    img = models.URLField()
    calories = models.TextField(max_length=500)
    fat = models.TextField(max_length=500)
    carbs = models.TextField(max_length=500)
    protein = models.TextField(max_length=500)
    cholesterol = models.TextField(max_length=500)
    sodium = models.TextField(max_length=500)
    sugar = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.title)