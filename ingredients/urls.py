from django.urls import path
from . import views
# from .views import (IngredientsListView)

urlpatterns = [
    path('', views.recipe_search, name="home"),
    path('select/', views.post, name='select'),
    path('favorites/', views.favorites, name='favorites')
    # path('apitest/', views.search_for_recipe, name='apitest')
]