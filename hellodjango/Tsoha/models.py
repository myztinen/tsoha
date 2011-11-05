from django.db import models

class Drink(models.Model):
    drinkType = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.drinkType
# Create your models here.
