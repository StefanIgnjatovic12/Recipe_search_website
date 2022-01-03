from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#In order to add fields to an existing form, we need to create a new form that inherits from the original form
#In this case the UserCreationForm is a default form but it doesn't have an email field
class UserRegisterForm(UserCreationForm):
    #additional field we want in addition to the inherited fields
    email = forms.EmailField()

    class Meta:
        #the model we want the form to interact with > when this form validates or saves, it creates a new instance of User
        model = User
        #fields that will be shown on the form and in what order
        fields = ['username', 'email', 'password1', 'password2']

#ModelForm is a helper class that lets you create a Form class from a Django model.
#Models are classes in django that are mapped to the database > each attribute corresponds to a database field
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['img']