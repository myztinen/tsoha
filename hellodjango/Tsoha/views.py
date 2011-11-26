from django.template import Context, RequestContext, loader
from Tsoha.models import Drink, Drink_name, Drink_type, Ingredient, Ingredient_Amount
from Tsoha.forms import SearchForm, AddRecipeForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from Tsoha.validators import AddRecipeValidator
from Tsoha.handlers import AddRecipeHandler
    
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
            form = SearchForm()

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
    c = RequestContext( request, {
        'ingredients' : ingredients,
    })
    return HttpResponse(t.render(c))
    
def add_recipe(request):
    if AddRecipeValidator(request).isValidAddRecipeRequest():
        form = AddRecipeForm(request.POST)
        if form.is_valid():
           AddRecipeHandler(form).saveRecipe()
           t = loader.get_template('add_recipe.html')
           c = RequestContext( request, {
                'ingredients' : ingredients,
                'message' : 'Drinkkireseptin talletus onnistui!',
           })
           return HttpResponse(t.render(c))
           
    else:
       ingredients = Ingredient.objects.all()
       t = loader.get_template('add_recipe.html')
       c = RequestContext( request, {
            'ingredients' : ingredients,
            'message' : 'Drinkkireseptin pakollisina tietoina on annettav juoman nimi, valmistusohjeet, juomatyyppi ja ainakin yksi ainesosa ja sen annos'
       })
       return HttpResponse(t.render(c)) 
       
       
def open_loginpage(request):
    t = loader.get_template('login.html')
    c = RequestContext( request, {
        'message' : 'Syota kayttajatunnus ja salasana',
    })
    return HttpResponse(t.render(c))
    
def log_user(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                t = loader.get_template('index.html')
                c = RequestContext( request, {
                 'message' : 'Kirjatuminen onnistui!',
                })
                return HttpResponse(t.render(c))
            else:
                t = loader.get_template('login.html')
                c = RequestContext( request, {
                    'message' : 'Tunnus on poissa kaytosta, pyyda yllapitajaa aktivoimaan se',
                })
                return HttpResponse(t.render(c))
        else:
            t = loader.get_template('login.html')
            c = RequestContext( request, {
                'message' : 'Vaara kayttajatunnus tai salasana',
            })
            return HttpResponse(t.render(c))

