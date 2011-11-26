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
        namecount = 0
        print namecount
        if namecount is 0:
            initial = Drink(recipe=self.drink_recipe, drink_type=drink_type)
            initial.save()
            second = Drink_name(name=self.drink_name, drink=initial)
            second.save()
            ingredient = Ingredient.objects.get(id=self.first_ingredient)
            print ingredient.name
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
                
            
            

 
               


             
    """    drink_name = forms.CharField(max_length=30)
        drink_recipe = forms.CharField(max_length=500)
        drink_type = forms.CharField(max_length=30)
        first_ingredient = forms.CharField(max_length=30)
        first_amount = forms.CharField(max_length=30)
        second_ingredient = forms.CharField(max_length=30)
        second_amount = forms.CharField(max_length=30)
        third_ingredient = forms.CharField(max_length=30)
        third_amount = forms.CharField(max_length=30)
        fourth_ingredient = forms.CharField(max_length=30)
        fourth_amount = forms.CharField(max_length=30)"""

