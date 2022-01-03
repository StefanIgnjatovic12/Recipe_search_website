from django.db import models

class SelectedIngredients (models.Model):
    food = models.CharField(max_length=500)

    def __str__(self):
        return str(self.food)