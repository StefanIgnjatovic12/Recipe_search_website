from django import forms
from .models import Ingredients
class IngredientButton(forms.Form):
    btn = forms.CharField()
