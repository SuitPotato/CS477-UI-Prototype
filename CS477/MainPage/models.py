from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Food(models.Model):
	foodID = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 35)
	price = models.FloatField()
	description = models.CharField(max_length = 150)
	uploadTime = models.DateTimeField(auto_now_add = True)
	
class Drink(models.Model):
	drinkID = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 35)
	price = models.FloatField()
	description = models.CharField(max_length = 150)
	uploadTime = models.DateTimeField(auto_now_add = True)
	