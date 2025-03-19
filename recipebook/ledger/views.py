from django.shortcuts import render
from . import models

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def recipeinDatabase(request):
    recipes = models.Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'recipelist.html', ctx)

def recipe_detail(request, pk):
    recipe = models.Recipe.objects.get(pk=pk)
    ctx = {'recipe': recipe}
    return render(request, 'recipedetail.html', ctx)

class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipelist.html'


class RecipeDetailView(DetailView):
    model = models.Recipe
    template_name = 'recipedetail.html'


