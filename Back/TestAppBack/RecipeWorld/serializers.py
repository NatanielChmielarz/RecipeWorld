from rest_framework import serializers
from RecipeWorld.models import Dish, Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'author', 'ingredients', 'instructions')


class DishSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'recipes')