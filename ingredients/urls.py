from django.urls import path
from . import views
# from .views import (IngredientsListView)

urlpatterns = [
    path('', views.ingredients_list_view, name="test"),
    path('select/', views.post, name='select'),
]