from django.urls import path
from . import views
# from .views import (IngredientsListView)

urlpatterns = [
    path('', views.home, name="home"),
    path('choicesstatus/', views.choices_status, name='choices'),
    path('search/', views.recipe_search, name="search"),
    path('select/', views.post, name='select'),
    path('favorites/', views.favorites, name='favorites')
    # path('apitest/', views.search_for_recipe, name='apitest')
]