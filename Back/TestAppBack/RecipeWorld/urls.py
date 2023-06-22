from django.urls import path
from RecipeWorld import views

urlpatterns = [
    path('dish/', views.dish_list),
    path('dish/<int:pk>/', views.dish_detail),
    path('recipe/', views.recipe_list),
    path('recipe/<int:pk>/', views.recipe_detail),
]