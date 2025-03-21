from django.shortcuts import render
from . import models
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

@login_required
def recipeinDatabase(request):
    recipes = models.Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'recipelist.html', ctx)

def recipeDetail(request, pk):
    recipe = models.Recipe.objects.get(pk=pk)
    ctx = {'recipe': recipe}
    return render(request, 'recipedetail.html', ctx)

class RecipeDetailView(DetailView):
    model = models.Recipe
    template_name = 'recipedetail.html'


