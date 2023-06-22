from django.db import models

class Recipe(models.Model):
    author = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()

    

class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    recipes = models.ManyToManyField(Recipe)

   