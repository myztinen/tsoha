from django.template import Context, RequestContext, loader
from Tsoha.models import Drink, Drink_name, Drink_type, Ingredient, Ingredient_Amount
from Tsoha.forms import SearchForm
from django.http import HttpResponse
from django.shortcuts import render

def index2(request):
    return render(request,'index.html')
    
def index(request):
    if request.method == 'GET': 
        form = SearchForm(request.GET) 
        if form.is_valid():
            parameter = form.cleaned_data['search_parameter']
            target = form.cleaned_data['search_target']
            
            if target == "ingredient":                            
                results = Drink_name.objects.select_related().filter(drink__ingredient_amount__ingredient__name__contains=parameter)
            else:
                results = Drink_name.objects.select_related().filter(name__contains=parameter)
            
            print results.values()
            
            t = loader.get_template('index.html')
            c = RequestContext( request, {
                'drink':results,
            })
            return HttpResponse(t.render(c))
        else:
            form = SearchForm() # An unbound form

    return render(request,'index.html')
    
def open_recipepage(request, recipe_id):
    drink = Drink.objects.select_related().get(id=recipe_id)
    amounts = Ingredient_Amount.objects.filter(drink=recipe_id)
    drink_names = drink.drink_name_set.all()
    t = loader.get_template('recipe.html')
    c = Context({
        'drink':drink,
        'amounts': amounts,
        'drink_names' : drink_names
    })
    return HttpResponse(t.render(c))
    
def open_addpage(request):
    ingredients = Ingredient.objects.all()
    t = loader.get_template('add_recipe.html')
    c = Context({
        'ingredients' : ingredients,
    })
    return HttpResponse(t.render(c))
    
    
    
    
    
    
def search(request):
    if request.method == 'POST': 
        form = SearchForm(request.POST) 
        if form.is_valid():
            parameter = form.cleaned_data['search_parameter']
            target = form.cleaned_data['search_target']
            

            if target == "ingredient":            
                result = Drink_name.objects.filter(drink__ingredient_amount__ingredient__name=parameter)
            else:
                result = Drink_name.objects.filter(name__contains=parameter)
            print result
            
            return HttpResponse(t.render(c))
    else:
        form = SearchForm() # An unbound form

    return HttpResponse("Posting was failure") 

