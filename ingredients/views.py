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
    context = {
        'ingredients':Ingredients.objects.all(),
        'groups': FoodGroups.objects.all()
    }

    return render(request, 'ingredients/test.html', context)


# class IngredientsListView(ListView):
#     model = Ingredients
#     template_name = 'ingredients/test.html'
#     context_object_name = 'ingredients'
#     paginate_by = 5
@csrf_exempt
def post(request):
    obj = SelectedIngredients()

    if request.POST.get('reload') == 'true':
        print('detected reload')
        SelectedIngredients.objects.all().delete()
        print(SelectedIngredients.objects.all())

    elif request.POST.get('testvalue') == 'check':
        id = request.POST.get('value')

        try:
            check = SelectedIngredients.objects.get(food=id)
        except ObjectDoesNotExist:
            check = None

        if check == None:
            obj.food = id
            obj.save()
            print(obj.food)
            print(SelectedIngredients.objects.all())

        elif check in SelectedIngredients.objects.all():
            check.delete()
            print(SelectedIngredients.objects.all())

    return JsonResponse({'test': 'test'})

def search_for_recipe(request):
    if(request.GET.get('mybtn')):
        ing_list = []

        for item in SelectedIngredients.objects.all():
            ing_list.append(item.food)

        api_key = '70b0e02384834d1db2b66fb35bd97984'
        params = {
            'apiKey':api_key,
            'number':3,
            'ingredients':ing_list
        }

        response = requests.get(url='https://api.spoonacular.com/recipes/findByIngredients', params=params)
        response.raise_for_status()
        recipes1 = json.loads(response.content)

        # first API Call just gets ID and ingredient list, have to use the ID for a second API call to get detailed info
        # Append all the IDs to a list and then use it as a parameter
        id_list = []
        for recipe in recipes1:
            id_list.append(str(recipe['id']))

        params2 =  {
            'apiKey':api_key,
            'ids':",".join(id_list),
            'includeNutrition': True
        }
        response2 = requests.get(url='https://api.spoonacular.com/recipes/informationBulk', params=params2)
        response2.raise_for_status()
        recipes2 = json.loads(response2.content)

        # generate recipes objects using the json data upon API call
        obj = DisplayRecipe()
        for recipe2 in recipes2:
            obj.title = recipe2['title']
            obj.link = recipe2['sourceUrl']
            obj.img = recipe2['image']
            obj.calories = recipe2['nutrition']['nutrients'][0]['amount']
            obj.fat = recipe2['nutrition']['nutrients'][1]['amount']
            obj.saturated_fat = recipe2['nutrition']['nutrients'][2]['amount']
            obj.carbs = recipe2['nutrition']['nutrients'][3]['amount']
            obj.protein = recipe2['nutrition']['nutrients'][8]['amount']
            obj.sodium = recipe2['nutrition']['nutrients'][7]['amount']
            obj.sugar = recipe2['nutrition']['nutrients'][5]['amount']
            # obj.ingredients = (
            #     for num in range(len(recipe2['nutrition']['ingredients'])):
            #         for ingredient in recipe2['nutrition']['ingredients'][num]:
            #
            # )
            print(obj.title)
            obj.save()
            print(DisplayRecipe.objects.all())
        print(DisplayRecipe.objects.all())
        return render(request, 'ingredients/apitest.html', {'recipes': recipes2})
    return render(request, 'ingredients/apitest.html')

