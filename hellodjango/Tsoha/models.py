from django.db import models

class Drink(models.Model):
    drink_type = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.drink_type
        
class Drink_name(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name
    
class DrinkToName(models.Model):
    drink_id = models.ForeignKey(Drink)
    drink_name_id = models.ForeignKey(Drink_name)

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name
    
class DrinkToIngredient(models.Model):
    drink_id = models.ForeignKey(Drink)
    ingredient_id = models.ForeignKey(Ingredient)
# Create your models here.
