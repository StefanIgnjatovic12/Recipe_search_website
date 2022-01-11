from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.views.generic import (ListView)
from ingredients.models.modelsIngredients import Ingredients, FoodGroups
from ingredients.models.modelSelected import SelectedIngredients
from ingredients.models.modelsRecipe import DisplayRecipe, FavoriteRecipe
from .forms import IngredientButton
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import requests
import json


@csrf_exempt
def ingredients_list_view(request):
    if request.GET.get('mybtn'):
        # API call code
        params={
            'apiKey':'70b0e02384834d1db2b66fb35bd97984',

            'includeIngredients': (',').join(request.session['choices']),
            'addRecipeNutrition': True,
            'fillIngredients': True,

            'number': 10,
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
        context = {
            'ingredients' : Ingredients.objects.all(),
            'groups' : FoodGroups.objects.all(),

        }

        return render(request, 'ingredients/test.html', context)
    return render(request, 'ingredients/test.html', context)


@csrf_exempt
def post(request):
    if request.POST.get('reload') == 'true':
        print('detected reload')
        try:
            # del request.session['choices']
            # del request.session['results']
            request.session.modified = True
            print('deleted')
        except KeyError:
            pass


    elif request.POST.get('testvalue') == 'check':
        id = request.POST.get('value')

        if request.POST.get('button_value') == 'green':

            selected_ingredients  = request.session.get('choices', [])
            selected_ingredients.insert(len(selected_ingredients), id)
            request.session['choices'] = selected_ingredients

            print(selected_ingredients)

        elif request.POST.get('button_value') == 'gray':

            selected_ingredients = request.session.get('choices', [])
            selected_ingredients.remove(id)
            request.session['choices'] = selected_ingredients

            print(selected_ingredients)


        # try:
        #     check = SelectedIngredients.objects.get(food=id)
        # except ObjectDoesNotExist:
        #     check = None
        #
        # if check == None:
        #     obj.food = id
        #     obj.save()
        #     print(obj.food)
        #     print(SelectedIngredients.objects.all())
        #
        # elif check in SelectedIngredients.objects.all():
        #     check.delete()
        #     print(SelectedIngredients.objects.all())

    return JsonResponse({'test': 'test'})

