from django import forms
from django.forms import ModelForm
from MainPage.models import Food, Drink

class FoodForm(forms.Form):
	class Meta:
		model = Food
		fields = ['name','price','description']
		
	name = forms.CharField(max_length=35)
	price = forms.FloatField()
	description = forms.CharField(max_length=150)
	

class DrinkForm(forms.Form):
	class Meta:
		model = Drink
	fields = ['name','price','description']
		
	name = forms.CharField(max_length=35)
	price = forms.FloatField()
	description = forms.CharField(max_length=150)



