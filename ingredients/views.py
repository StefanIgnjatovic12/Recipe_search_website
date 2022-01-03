from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.views.generic import (ListView)
from ingredients.models.modelsIngredients import Ingredients
from ingredients.models.modelSelected import SelectedIngredients
from .forms import IngredientButton
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json


@csrf_exempt
def ingredients_list_view(request):
    ingredients = Ingredients.objects.all()
    return render(request, 'ingredients/test.html', {'ingredients': ingredients})


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
