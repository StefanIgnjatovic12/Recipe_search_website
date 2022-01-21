from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import JsonResponse
from ingredients.models.modelsIngredients import Ingredients, FoodGroups
from ingredients.models.modelsRecipe import FavoriteRecipe
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test

import requests
import json
import os

from .forms import SubmitButton

# @csrf_exempt
# When mybtn clicked, api is called and the results are saved to session
# @user_passes_test(lambda u: u.is_superuser)
def recipe_search(request):
    if request.POST.get('mybtn'):

        form = SubmitButton(request.POST)
        if form.is_valid():
            params = {
                # 'apiKey': '70b0e02384834d1db2b66fb35bd97984',
                'apiKey': os.environ.get('SECRET_KEY'),
                'includeIngredients': ','.join(request.session['choices']),
                'addRecipeNutrition': True,
                'fillIngredients': True,
                'addRecipeInformation': True,
                'number': 4,
                'sort': 'min-missing-ingredients',
                'sortDirection': 'desc'

            }

            response = requests.get(url='https://api.spoonacular.com/recipes/complexSearch', params=params)
            response.raise_for_status()
            print(response.elapsed.total_seconds())

            recipes = json.loads(response.content)
            # created 2 session for the same result because need it to stay available for favoriting but it gets deleted
            # upon page reload which happens every time a search is done. so have another session data that is the same
            # but doesnt get deleted until after the object is saved
            request.session['results'] = recipes['results']
            request.session['favorite'] = recipes['results']

            return redirect('home')




# @csrf_exempt

def post(request):
    # checks AJAX to see if the page has been reloaded
    # if page has been reloaded, clear the results data from the session so the same recipes aren't shown again
    if request.POST.get('reload') == 'true':
        print('detected reload')
        try:
            # not deleting choices means that if you click submit with nothing selected the search still goes through
            # not deleting results means that if you refresh the page you'll have the same recipes left
            del request.session['choices']
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
            request.session.modified = True
            print(selected_ingredients)
            print('green')
        # checks if the button is gray ie unselected > if yes, removes the value/ingredient name
        # for that button from the choices list
        elif request.POST.get('button_color') == 'gray':

            selected_ingredients = request.session.get('choices', [])
            if ingredients_name in selected_ingredients:
                selected_ingredients.remove(ingredients_name)
                request.session['choices'] = selected_ingredients
                print(selected_ingredients)
                print('gray')

    elif request.POST.get('recipe_id') is not None:
        print('received counter_button click')
        recipe_id = request.POST.get('recipe_id')
        print(recipe_id)
        if FavoriteRecipe.objects.filter(id=recipe_id).exists():
            FavoriteRecipe.objects.filter(id=recipe_id).delete()
        else:
            obj = FavoriteRecipe.objects.create(user=request.user,
                                                title=request.session['favorite'][int(recipe_id)]['title'],
                                                ready_in=request.session['favorite'][int(recipe_id)]['readyInMinutes'],
                                                link=request.session['favorite'][int(recipe_id)]['sourceUrl'],
                                                img=request.session['favorite'][int(recipe_id)]['image'],
                                                cuisines=request.session['favorite'][int(recipe_id)]['cuisines'],
                                                used_ingredient_count=request.session['favorite'][int(recipe_id)][
                                                    'usedIngredientCount'],
                                                used_ingredients=request.session['favorite'][int(recipe_id)][
                                                    'usedIngredients'],
                                                missed_ingredients=request.session['favorite'][int(recipe_id)][
                                                    'missedIngredients'],
                                                missed_ingredient_count=request.session['favorite'][int(recipe_id)][
                                                    'missedIngredientCount'],
                                                servings=request.session['favorite'][int(recipe_id)][
                                                    'servings'],
                                                calories=request.session['favorite'][int(recipe_id)]['nutrition']['nutrients'][0]['amount'],
                                                fat=request.session['favorite'][int(recipe_id)]['nutrition']['nutrients'][1]['amount'],
                                                carbs=request.session['favorite'][int(recipe_id)]['nutrition']['nutrients'][3]['amount'],
                                                protein=request.session['favorite'][int(recipe_id)]['nutrition']['nutrients'][8]['amount'],
                                                sodium=request.session['favorite'][int(recipe_id)]['nutrition']['nutrients'][7]['amount'],
                                                sugar=request.session['favorite'][int(recipe_id)]['nutrition']['nutrients'][5]['amount']
                                                )

            obj.save()
            try:
                del request.session['favorite']
            except KeyError:
                pass

    return JsonResponse({'test': 'test'})

def favorites(request):
    context = {'favorites': FavoriteRecipe.objects.all()}
    return render(request, 'ingredients/favorites.html', context)

def about(request):
    return render (request, 'ingredients/about.html', {'title': 'about'})

# if there is a key 'results" in request.session, render the page with it (ie after a search)
# if there isn't render it without it ie pre search and post refresh
def home(request):
    if 'results' in request.session:
        context = {
            'recipes': request.session['results'],
            'ingredients': Ingredients.objects.all(),
            'groups': FoodGroups.objects.all(),

        }
        return render(request, 'ingredients/home.html', context)

    else:
        context = {

            'ingredients': Ingredients.objects.all(),
            'groups': FoodGroups.objects.all(),

        }
        return render(request, 'ingredients/home.html', context)



def choices_status(request):
    try:
        print(request.session['choices'])
        print('full')
        return JsonResponse({'choices': 'full'})

    except KeyError:
        print('empty')
        return JsonResponse({'choices':'empty'})
