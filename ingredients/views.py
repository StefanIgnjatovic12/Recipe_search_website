from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.views.generic import (ListView)
from ingredients.models.modelsIngredients import Ingredients, FoodGroups
from ingredients.models.modelsRecipe import FavoriteRecipe
from django.views.decorators.csrf import csrf_exempt
import requests
import json


@csrf_exempt
def recipe_search(request):
    if request.GET.get('mybtn'):
        # API call code
        params = {
            'apiKey': '70b0e02384834d1db2b66fb35bd97984',

            'includeIngredients': ','.join(request.session['choices']),
            'addRecipeNutrition': True,
            'fillIngredients': True,
            'addRecipeInformation': True,
            'number': 2,
            'sort': 'max-used-ingredients',
            'sortDirection': 'desc'

        }

        response = requests.get(url='https://api.spoonacular.com/recipes/complexSearch', params=params)
        response.raise_for_status()
        print(response.elapsed.total_seconds())

        recipes = json.loads(response.content)
        request.session['results'] = recipes['results']

        context = {
            'recipes': request.session['results'],
            'ingredients': Ingredients.objects.all(),
            'groups': FoodGroups.objects.all()
        }

    else:
        # if recipes is in here, you will see the recipes that are saved in the results
        context = {
            'recipes': request.session['results'],
            'ingredients': Ingredients.objects.all(),
            'groups': FoodGroups.objects.all(),

        }

        return render(request, 'ingredients/test.html', context)
    return render(request, 'ingredients/test.html', context)


@csrf_exempt
def post(request):
    # checks AJAX to see if the page has been reloaded
    # if page has been reloaded, clear the results data from the session so the same recipes aren't shown again
    if request.POST.get('reload') == 'true':
        print('detected reload')
        try:
            # not deleting choices means that if you click submit with nothing selected the search still goes through
            # not deleting results means that if you refresh the page you'll have the same recipes left
            # del request.session['choices']
            # del request.session['results']
            request.session.modified = True
            print('deleted')
        except KeyError:
            pass
    # checks AJAX to see if a button has been clicked
    #if it has, gets the value of the button which is the ingredient name
    elif request.POST.get('button_state') == 'clicked':
        ingredients_name = request.POST.get('value')

        # checks if the button is green ie selected > if yes, it creates a list and inserts the
        # buttons value/the ingredient name
        if request.POST.get('button_color') == 'green':

            selected_ingredients = request.session.get('choices', [])
            selected_ingredients.insert(len(selected_ingredients), ingredients_name)
            request.session['choices'] = selected_ingredients

            print(selected_ingredients)
            print('green')
        # checks if the button is gray ie unselected > if yes, removes the value/ingredient name
        # for that button from the choices list
        elif request.POST.get('button_color') == 'gray':

            selected_ingredients = request.session.get('choices', [])
            selected_ingredients.remove(ingredients_name)
            request.session['choices'] = selected_ingredients

            print(selected_ingredients)
            print('gray')
    # If the favorite button is clicked, the index of the recipe within the request.session['results']
    # is passed through; can then create an object based on these
    # TEST AGAIN
    if request.POST.get('recipe_id') is not None:
        print('received counter_button click')
        recipe_id = request.POST.get('recipe_id')
        print(recipe_id)
        # obj = FavoriteRecipe()
        # obj.title = request.session['results'][int(recipe_id)]['title']
        # obj.user = request.user
        # obj.save()


    return JsonResponse({'test': 'test'})
