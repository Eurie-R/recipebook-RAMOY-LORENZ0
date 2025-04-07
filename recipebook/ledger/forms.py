from django import forms
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe 
        fields = '__all__'

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class ImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = '__all__'
