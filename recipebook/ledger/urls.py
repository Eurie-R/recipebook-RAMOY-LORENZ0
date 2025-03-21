from django.urls import path 
from .views import RecipeDetailView , recipeinDatabase

urlpatterns = [
    path('', recipeinDatabase, name='recipe_list'),
    path('recipes/list/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),

]

app_name = "ledger"