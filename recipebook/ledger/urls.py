from django.urls import path 
from .views import RecipeDetailView , recipe_list, recipe_add, add_image

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('recipes/list/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/add', recipe_add, name = 'recipe_add' ),
    path('recipe/<int:pk>/add_image', add_image , name = 'image_add' )

] 

app_name = "ledger"