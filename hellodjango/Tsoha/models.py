from django.db import models

class Drink(models.Model):
    drink_type = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.drink_type
# Create your models here.
