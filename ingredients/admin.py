from django.contrib import admin
from ingredients.models.modelsIngredients import Ingredients
from ingredients.models.modelsRecipe import FavoriteRecipe

admin.site.register(Ingredients)
admin.site.register(FavoriteRecipe)