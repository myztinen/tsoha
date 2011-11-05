from Tsoha.models import Drink
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. you are at my testpage")
    
def save_test(request):
    drinksu = Drink(drink_type="outoJuoma")
    drinksu.save()
    return HttpResponse("Hello, world. testing saving")
