from django.db import models

class AbstractRecipeModel(models.Model):
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

    class Meta:
        abstract = True

class DisplayRecipe (AbstractRecipeModel):
    pass
class FavoriteRecipe (AbstractRecipeModel):
    # add many to one with logged in user class
    pass

