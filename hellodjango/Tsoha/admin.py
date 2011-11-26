from Tsoha.models import Drink, Drink_name, Drink_type, Ingredient, Ingredient_Amount
from django.contrib import admin

"""
admin.site.register(Drink_name)
admin.site.register(Drink_type)
admin.site.register(Ingredient)
admin.site.register(Ingredient_Amount)
"""
class DrinkAdmin(admin.ModelAdmin):
    fields = ['recipe', 'drink_type']
    
class DrinkNameAdmin(admin.ModelAdmin):
    fields = ['name', 'drink']
    
class IngredientAdmin(admin.ModelAdmin):
    fields = ['name']

class DrinkTypeAdmin(admin.ModelAdmin):
    fields = ['type_name']
    
admin.site.register(Drink, DrinkAdmin)
admin.site.register(Drink_name,DrinkNameAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Drink_type, DrinkTypeAdmin)
