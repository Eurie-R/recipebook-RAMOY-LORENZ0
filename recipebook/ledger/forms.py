from django import forms
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage

class recipe_form(forms.ModelForm):
    class Meta:
        model = Recipe 
        fields = '__all__'

class OtherRecipeForm(forms.Form):
    ingredient = forms.CharField(label='Recipe name', max_length=100)
    recipe = forms.ModelChoiceField(label='Recipe', queryset=Recipe.objects.all())

class recipe_ingredientform(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'

class ingredient_form(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class image_form(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = '__all__'
