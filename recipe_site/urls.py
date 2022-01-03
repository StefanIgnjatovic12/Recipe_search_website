from django.urls import path
from . import views
from .views import (RecipeListView,
                    SingleRecipeDetailView,
                    SingleRecipeCreateView,
                    SingleRecipeUpdateView,
                    SingleRecipeDeleteView,
                    UserRecipeListView)

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    #the "username" here is being passed into the get_queryset() method in the views file
    #so that we can filter and display recipes made by that user
    path('user/<str:username>', UserRecipeListView.as_view(), name='user-recipes'),
    path('recipe/<int:pk>/', SingleRecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/new/', SingleRecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/update/', SingleRecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/', SingleRecipeDeleteView.as_view(), name='recipe-delete'),
    path('about/', views.about, name="about")

    ]