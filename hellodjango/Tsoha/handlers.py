# coding: utf-8
from django.template import Context, RequestContext, loader
from Tsoha.models import Drink, Drink_name, Drink_type, Ingredient, Ingredient_Amount
from Tsoha.forms import SearchForm, AddRecipeForm
from django.http import HttpResponse
from django.shortcuts import render

class AddRecipeHandler():
    def __init__(self, form):
        self.form = form       
        self.drink_name = form.cleaned_data['drink_name']
        self.drink_type = form.cleaned_data['drink_type']
        self.drink_recipe = form.cleaned_data['drink_recipe']
        self.first_ingredient = form.cleaned_data['first_ingredient']
        self.first_amount = form.cleaned_data['first_amount']
        self.second_ingredient = form.cleaned_data['second_ingredient']
        self.second_amount = form.cleaned_data['second_amount']      
        self.third_ingredient = form.cleaned_data['third_ingredient']
        self.third_amount = form.cleaned_data['third_amount']
        self.fourth_ingredient = form.cleaned_data['fourth_ingredient']
        self.fourth_amount = form.cleaned_data['fourth_amount']                    
        
    def saveRecipe(self):
        drink_type = Drink_type.objects.get(id=self.drink_type)
        namecount = Drink_name.objects.filter(name__iexact=self.drink_name).count()
        if namecount is 0 and self.hasUniqueIngredients():
            initial = Drink(recipe=self.drink_recipe, drink_type=drink_type)
            initial.save()
            second = Drink_name(name=self.drink_name, drink=initial)
            second.save()
            ingredient = Ingredient.objects.get(id=self.first_ingredient)
            ingredient_am = Ingredient_Amount(drink=initial, amount = self.first_amount,  ingredient=ingredient)
            ingredient_am.save()
            if self.second_ingredient and self.second_amount:
                ingredient = Ingredient.objects.get(id=self.second_ingredient)
                ingredient_am = Ingredient_Amount(drink=initial, amount = self.second_amount,  ingredient=ingredient)
                ingredient_am.save()
            if self.third_ingredient and self.third_amount:
                ingredient = Ingredient.objects.get(id=self.third_ingredient)
                ingredient_am = Ingredient_Amount(drink=initial, amount = self.third_amount,  ingredient=ingredient)
                ingredient_am.save()
            if self.fourth_ingredient and self.fourth_amount:
                ingredient = Ingredient.objects.get(id=self.fourth_ingredient)
                ingredient_am = Ingredient_Amount(drink=initial, amount = self.fourth_amount,  ingredient=ingredient)
                ingredient_am.save()
            return 'Drinkkireseptin talletus onnistui!'
        elif namecount is not 0 and self.hasUniqueIngredients():
            return 'Samanniminen resepti on jo olemassa. Reseptiä ei talletettu'
        else:
            return 'Ainesosa saa esiintyä reseptissä vain yhden kerran. Reseptiä ei talletettu.'
    
    def hasUniqueIngredients(self):
        ingredients = filter(lambda x: x !='NULL', [self.first_ingredient, self.second_ingredient, self.third_ingredient, self.fourth_ingredient])
        ingredient_set = list(set(ingredients))
        if len(ingredient_set) is len(ingredients):
            return True
        else:
            return False
                
            
  

