from django.db import models

class Drink_type(models.Model):
    type_name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.type_name
        
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

class Drink(models.Model):
    drink_type = models.ForeignKey(Drink_type)
    recipe = models.CharField(max_length=500)
    ingredients = models.ManyToManyField(Ingredient, through='Ingredient_Amount')
    
    def __unicode__(self):
        return self.drink_type

class Drink_name(models.Model):
    name = models.CharField(max_length=30)
    drink = models.ForeignKey(Drink)
    
    def __unicode__(self):
        return self.name
    
class Ingredient_Amount(models.Model):
    drink = models.ForeignKey(Drink)
    amount = models.CharField(max_length=30)
    ingredient = models.ForeignKey(Ingredient)
    
    def __unicode__(self):
        return self.amount
# Create your models here.
