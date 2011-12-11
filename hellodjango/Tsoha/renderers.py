# coding: utf-8
from django.template import Context, RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import render

class IndexPageRenderer:
    def __init__(self, request):
        self.request = request
    
    def renderIndexPage(self, results=None, message=None):
        t = loader.get_template('index.html')
        c = RequestContext( self.request, {
            'drink':results,
            'user' : self.request.user,
            'message' : message,
        })
        return HttpResponse(t.render(c))
        
class LoginPageRenderer:
    def __init__(self,request):
        self.request = request
        
    def renderLoginPage(self, message=None):
        t = loader.get_template('login.html')
        c = RequestContext( self.request, {
            'message' : message,
        })
        return HttpResponse(t.render(c))


class AddRecipePageRenderer:
    def __init__(self,request):
        self.request = request
    
    def renderAddRecipePage(self, ingredients, drink_types, message=None):
        t = loader.get_template('add_recipe.html')
        c = RequestContext( self.request, {
            'ingredients' : ingredients,
            'drink_types' : drink_types,
            'message' : message,
        })
        return HttpResponse(t.render(c)) 
        
class RecipePageRenderer:
    
    def renderRecipePage(self, drink, amounts, drink_names):
        t = loader.get_template('recipe.html')
        c = Context({
            'drink':drink,
            'amounts': amounts,
            'drink_names' : drink_names
        })
        return HttpResponse(t.render(c))
