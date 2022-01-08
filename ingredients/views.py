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
        lst=[]
        for recipe2 in recipes2:
            title = recipe2['title']
            link = recipe2['sourceUrl']
            img = recipe2['image']
            calories = recipe2['nutrition']['nutrients'][0]['amount']
            fat = recipe2['nutrition']['nutrients'][1]['amount']
            saturated_fat = recipe2['nutrition']['nutrients'][2]['amount']
            carbs = recipe2['nutrition']['nutrients'][3]['amount']
            protein = recipe2['nutrition']['nutrients'][8]['amount']
            sodium = recipe2['nutrition']['nutrients'][7]['amount']
            sugar = recipe2['nutrition']['nutrients'][5]['amount']
            # creates list of dictionaries that hold the data for each recipe the was returned
            sorted_query_data = [{
                'amount': [d['amount'] for d in recipe2['nutrition']['ingredients']],
                'unit': [d['unit'] for d in recipe2['nutrition']['ingredients']],
                'name': [d['name'] for d in recipe2['nutrition']['ingredients']]

            }]
            # loops through the gdata and creates an f string with the amount, unit and name of the ingredients corresponding to each recipe then appends them to a list
            for number in range(len(sorted_query_data)):
                for n in range(len(sorted_query_data[number]['amount'])):
                    lst.append(f"{sorted_query_data[number]['amount'][n]} {sorted_query_data[number]['unit'][n]} of {sorted_query_data[number]['name'][n]}")
                i = DisplayRecipe.objects.create(
                    title=title,
                    link=link,
                    img=img,
                    calories=calories,
                    fat=fat,
                    saturated_fat=saturated_fat,
                    carbs=carbs,
                    protein=protein,
                    sodium=sodium,
                    sugar=sugar,
                    ingredients=", ".join(lst)
                )
                i.save()
                # clear the list after each loop corresponding to 1 recipe otherwise the ingredients for the next recipe are added to those of the firstru
                lst.clear()
        print(DisplayRecipe.objects.all())
        return render(request, 'ingredients/apitest.html', {'recipes': recipes2})
    return render(request, 'ingredients/apitest.html')

