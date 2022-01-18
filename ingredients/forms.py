from django import forms
from .models import Ingredients
class SubmitButton(forms.Form):
    mybtn = forms.CharField()
