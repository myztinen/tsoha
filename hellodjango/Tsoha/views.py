# coding: utf-8
from Tsoha.models import Drink, Drink_name, Drink_type, Ingredient, Ingredient_Amount
from Tsoha.forms import SearchForm, AddRecipeForm
from django.contrib.auth import authenticate, login, logout
from Tsoha.validators import AddRecipeValidator
from Tsoha.handlers import AddRecipeHandler
from Tsoha.renderers import RecipePageRenderer, AddRecipePageRenderer, LoginPageRenderer, IndexPageRenderer
    
def index(request):
    if request.method == 'GET': 
        form = SearchForm(request.GET) 
        if form.is_valid():
            parameter = form.cleaned_data['search_parameter']
            target = form.cleaned_data['search_target']
            
            if target == "ingredient":                            
                results = Drink_name.objects.select_related().filter(drink__ingredient_amount__ingredient__name__icontains=parameter).order_by('name')
            else:
                results = Drink_name.objects.select_related().filter(name__icontains=parameter).order_by('name')          
            return IndexPageRenderer(request).renderIndexPage(results)
        else:
            form = SearchForm()
    return IndexPageRenderer(request).renderIndexPage()
    
def open_recipepage(request, recipe_id):
    drink = Drink.objects.select_related().get(id=recipe_id)
    amounts = Ingredient_Amount.objects.filter(drink=recipe_id)
    drink_names = drink.drink_name_set.all()
    return RecipePageRenderer().renderRecipePage(drink, amounts, drink_names)
    
def open_addpage(request):
    if request.user.is_authenticated():
        ingredients = Ingredient.objects.all().order_by('name')
        drink_types = Drink_type.objects.all().order_by('type_name')
        return AddRecipePageRenderer(request).renderAddRecipePage(ingredients, drink_types)
    else:
        message = 'Sinun täytyy kirjautua lisätäksesi reseptejä'
        return IndexPageRenderer(request).renderIndexPage(None,message)
    
def add_recipe(request):
    if request.user.is_authenticated():
        ingredients = Ingredient.objects.all().order_by('name')
        drink_types = Drink_type.objects.all().order_by('type_name')
        if AddRecipeValidator(request).isValidAddRecipeRequest():
            form = AddRecipeForm(request.POST)
            if form.is_valid():
                message = AddRecipeHandler(form).saveRecipe()
                return AddRecipePageRenderer(request).renderAddRecipePage(ingredients, drink_types, message)
        else:
           message = 'Drinkkireseptin pakollisina tietoina on annettava juoman nimi, valmistusohjeet, juomatyyppi ja ainakin yksi ainesosa ja sen annos'

           return AddRecipePageRenderer(request).renderAddRecipePage(ingredients, drink_types, message)
    else:
        message = 'Sinun täytyy kirjautua lisätäksesi reseptejä'
        return IndexPageRenderer(request).renderIndexPage(None,message)
       
       
def open_loginpage(request):
    message = 'Syötä käyttäjätunnus ja salasana'
    
    return LoginPageRenderer(request).renderLoginPage(message)
    
def log_user(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                message = 'Kirjautuminen onnistui!'
                return IndexPageRenderer(request).renderIndexPage(None,message)
            else:
                message = 'Tunnus on poissa käytösta, pyydä ylläpitäjää aktivoimaan se' 
                return LoginPageRenderer(request).renderLoginPage(message)
        else:
            message = 'Väärä käyttäjätunnus tai salasana'
            return LoginPageRenderer(request).renderLoginPage(message)

def logout_user(request):
    logout(request)
    message = 'Kirjauduit onnistuneesti ulos'
    return IndexPageRenderer(request).renderIndexPage(None,message)

