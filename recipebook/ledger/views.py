from django.shortcuts import render , redirect
from . import models
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .forms import recipe_form, ingredient_form, recipe_ingredientform, image_form

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
        #create the form 
        form = recipe_form(request.POST, request.FILES)
        #check if valid 
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    
    form = recipe_form()
    recipes = models.Recipe.objects.all()
    recipeIngredients = models.Recipe.objects.all()

    ctx = { "recipe": recipes, "recipeIngredients": recipeIngredients, "form": form }

    print(f"request type: {request.method}")
    print(f"ctx: {ctx}")

    return render(request, 'recipelist.html', {'recipes': recipes, 'recipe_form':form})

def recipe_add(request):
     if request.method == 'POST':
        #create the form 
        Recipeform = recipe_form(request.POST, request.FILES)
        IngredientForm = ingredient_form(request.POST)
        RecipeIngredientForm = recipe_ingredientform(request.POST)
        if Recipeform.is_valid():
            Recipeform.save()
            return redirect('ledger:recipe_list')
        elif IngredientForm.is_valid():
            IngredientForm.save()
            return redirect('ledger:recipe_list')
        elif RecipeIngredientForm.is_valid():
            RecipeIngredientForm.save()
            return redirect('ledger:recipe_list')
     else:
        RecipeForm = recipe_form()
        IngredientForm = ingredient_form()
        RecipeIngredientForm = recipe_ingredientform()
        recipeIngredients = models.Recipe.objects.all()

        ctx = { "recipeIngredients": recipeIngredients }

        print(f"request type: {request.method}")
        print(f"ctx: {ctx}")

        return render(request, 'addRecipe.html', {"recipe_form": RecipeForm, "ingredient_form": IngredientForm, "recipe_ingredient_form": RecipeIngredientForm})
     
def add_image(request, pk):
    if request.method == 'POST':
        #create the form 
        imgform = image_form(request.POST, request.FILES)
        if imgform.is_valid():
            imgform.save()
            return redirect('ledger:recipe_detail')
    else:
        imgForm = image_form()
        ctx = {'image_form':imgForm }

        return render(request, 'addImage.html',ctx)







