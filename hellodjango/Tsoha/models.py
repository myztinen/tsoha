from django.db import models

class Drink(models.Model):
    drink_type = models.CharField(max_length=30)
    recipe = models.CharField(max_length=500)
    
    def __unicode__(self):
        return self.drink_type
        
class Drink_name(models.Model):
    name = models.CharField(max_length=30)
    drink = models.ForeignKey(Drink)
    
    def __unicode__(self):
        return self.name
    

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name
    
class DrinkToIngredient(models.Model):
    drink = models.ForeignKey(Drink)
    amount = models.IntegerField(max_length=3)
    measurement = models.CharField(max_length=3)
    ingredient = models.ForeignKey(Ingredient)
# Create your models here.
