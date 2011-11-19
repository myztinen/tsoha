from django.template import Context, loader
from Tsoha.models import Drink, Drink_name, Drink_type, Ingredient, Ingredient_Amount
from Tsoha.forms import SearchForm
from django.http import HttpResponse
from django.shortcuts import render

def index2(request):
    return render(request,'index.html')
    
def index(request):
    drink = Drink.objects.select_related().get(id=33)
    amounts = Ingredient_Amount.objects.filter(drink=33)
    ingredients = drink.ingredients.all()
    drink_names = drink.drink_name_set.all()
    t = loader.get_template('index.html')
    c = Context({
        'drink':drink,
        'amounts': amounts,
        'drink_names' : drink_names
    })
    return HttpResponse(t.render(c))
    
def open_searchpage(request):
    return render(request,'search.html')
    
def open_addpage(request):
    return render(request,'add_recipe.html')
    
def search_test(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            parameter = form.cleaned_data['search_parameter']
            target = form.cleaned_data['search_target']
            print parameter

            if target == "ingredient":            
                result = Drink_name.objects.filter(drink__ingredient_amount__ingredient__name=parameter)
            else:
                result = Drink_name.objects.filter(name__contains=parameter)
            print result
            
            return HttpResponse("Posting was succeess") # Redirect after POST
    else:
        form = SearchForm() # An unbound form

    return HttpResponse("Posting was failure") 

