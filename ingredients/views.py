from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.views.generic import (ListView)
from ingredients.models.modelsIngredients import Ingredients, FoodGroups
from ingredients.models.modelSelected import SelectedIngredients
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
        # with open('testapireturn.json', 'w') as fp:
        #     json.dump(response.json(), fp)
        recipes = json.loads(response.content)
        # generate recipes objects using the json data upon API call
        return render(request, 'ingredients/apitest.html', {'recipes': recipes})
    return render(request, 'ingredients/apitest.html')
