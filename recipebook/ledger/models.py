from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Bio = models.CharField(max_length=255)

    def __str__(self):
        return self.Name
class Ingredient(models.Model):
    name = models.CharField(max_length=50)  

    def __str__(self):
        return self.name 


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    Author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class RecipeIngredient(models.Model):
    Quantity = models.CharField(max_length=50)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name= 'recipe')
    Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

