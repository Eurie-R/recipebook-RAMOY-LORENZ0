from django.contrib import admin
from .models import Recipe , RecipeIngredient , Ingredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    list_display = ["name"]
    list_filter = ["name"]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    list_display = ["name"]
    list_filter = ["name"]

class RecipeLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [RecipeLine]



admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeIngredientAdmin)