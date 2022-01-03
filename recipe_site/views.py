from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.models import User
from .models import Recipes

# def home(request):
#     context = {
#         "posts": Recipes.objects.all()
#     }
#     return render (request, 'recipe_site/home.html', context)

class RecipeListView(ListView):
    #tells list view what model to query to create the list
    model = Recipes
    #                <app>/<model>_<viewtype> is the default
    template_name = 'recipe_site/home.html'
    # changing the name of the list of blog posts that's being iterated over in the html file to gener
    context_object_name = 'posts'
    # ordering based on one of the attributes, minus sign makes it go from newest to oldest instead of default reverse
    ordering = ['-date_posted']
    paginate_by = 4

class UserRecipeListView(ListView):
    model = Recipes
    template_name = 'recipe_site/user_recipes.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self, *args, **kwargs):
        #the user that we want to get has a username thats equal to the one in the url we will pass
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Recipes.objects.filter(author=user).order_by('-date_posted')

#generic class used to see the individual posts themselves when you open them
class SingleRecipeDetailView(DetailView):
    model = Recipes

#generic class we're using to create the form
#Mixin - class that we inherit from that adds functionality to the view eg login is required to access route
class SingleRecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipes
    fields = ['title', 'content']


#before you submit the form, take the instance and set the author to be equal to the current logged in user
#then validate using super > before form_valid is run on the parent class
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Class to update posts, uses the same form and form_valid as the create class
#UserPassesTestMixin - so 1 user cant edit posts that other users made
class SingleRecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipes
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #for the UserPassesTextMixin
    def test_func(self):
        #get the recipe that we are trying to update
        recipe = self.get_object()
        #checks if current logged in user is the same as the author of the post
        if self.request.user == recipe.author:
            return True
        return False

#We want the user to both be logged in and the author of the post theyre trying to delete
class SingleRecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipes
    success_url = '/'

    def test_func(self):
        #get the recipe that we are trying to update
        recipe = self.get_object()
        #checks if current logged in user is the same as the author of the post
        if self.request.user == recipe.author:
            return True
        return False

def about(request):
    return render (request, 'recipe_site/about.html', {'title': 'about'})

