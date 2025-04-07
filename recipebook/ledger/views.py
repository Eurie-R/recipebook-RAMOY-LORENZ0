from django.shortcuts import render , redirect
from . import models
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm, ImageForm

@login_required
def recipe_detail(request, pk):
    recipe = models.Recipe.objects.get(pk=pk)
    return render(request, 'recipe_detail.html', {
        'recipe': recipe,
    })
class RecipeDetailView(DetailView):
    model = models.Recipe
    template_name = 'recipedetail.html'

@login_required
def recipe_list(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    
    form = RecipeForm()
    recipes = models.Recipe.objects.all()
    recipeIngredients = models.Recipe.objects.all()

    ctx = { "recipe": recipes, "recipeIngredients": recipeIngredients, "form": form }

    print(f"request type: {request.method}")
    print(f"ctx: {ctx}")

    return render(request, 'recipelist.html', {'recipes': recipes, 'recipe_form':form})

@login_required
def recipe_add(request):
     if request.method == 'POST':
        #create the form 
        recipeForm = RecipeForm(request.POST, request.FILES)
        ingredientForm = IngredientForm(request.POST)
        recipeIngredientForm = RecipeIngredientForm(request.POST)
        if recipeForm.is_valid():
            recipeForm.save()
            return redirect('ledger:recipe_list')
        elif ingredientForm.is_valid():
            ingredientForm.save()
            return redirect('ledger:recipe_list')
        elif recipeIngredientForm.is_valid():
            recipeIngredientForm.save()
            return redirect('ledger:recipe_list')
     else:
        recipeForm = RecipeForm()
        ingredientForm = IngredientForm()
        recipeIngredientForm = RecipeIngredientForm()
        recipeIngredients = models.Recipe.objects.all()

        ctx = { "recipeIngredients": recipeIngredients }

        print(f"request type: {request.method}")
        print(f"ctx: {ctx}")

        return render(request, 'addRecipe.html', {"recipe_form": recipeForm, "ingredient_form": ingredientForm, "recipe_ingredient_form": recipeIngredientForm})

@login_required 
def add_image(request, pk):
    if request.method == 'POST':
        #create the form 
        imgform = ImageForm(request.POST, request.FILES)
        if imgform.is_valid():
            imgform.save()
            return redirect('ledger:recipe_list')
    else:
        imgForm = ImageForm()
        ctx = {'image_form':imgForm }

        return render(request, 'addImage.html',ctx)







