from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from RecipeWorld.models import Dish, Recipe
from RecipeWorld.serializers import DishSerializer, RecipeSerializer


@csrf_exempt
def dish_list(request):
    if request.method == 'GET':
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        dish_data = JSONParser().parse(request)
        serializer = DishSerializer(data=dish_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def dish_detail(request, pk):
    try:
        dish = Dish.objects.get(pk=pk)
    except Dish.DoesNotExist:
        return JsonResponse({'error': 'Dish does not exist'}, status=404)

    if request.method == 'GET':
        serializer = DishSerializer(dish)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        dish_data = JSONParser().parse(request)
        serializer = DishSerializer(dish, data=dish_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dish.delete()
        return JsonResponse({'message': 'Dish deleted successfully'}, status=204)


@csrf_exempt
def recipe_list(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        recipe_data = JSONParser().parse(request)
        serializer = RecipeSerializer(data=recipe_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return JsonResponse({'error': 'Recipe does not exist'}, status=404)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        recipe_data = JSONParser().parse(request)
        serializer = RecipeSerializer(recipe, data=recipe_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        recipe.delete()
        return JsonResponse({'message': 'Recipe deleted successfully'}, status=204)