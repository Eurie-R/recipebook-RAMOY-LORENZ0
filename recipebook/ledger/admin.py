from django.contrib import admin
from .models import Recipe , RecipeIngredient , Ingredient , Profile, RecipeImage
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    
    list_display = ['Image','Description','Recipe']

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    list_display = ["name"]
    inlines = [RecipeImageInline]
    list_filter = ["name"]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    list_display = ["name"]
    list_filter = ["name"]


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    list_display = ["Quantity", "Ingredient", "Recipe"]

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
