from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from MainPage.models import Food, Drink
from MainPage.forms import FoodForm, DrinkForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
	return render(request, 'MainPage/index.html')
	
def about(request):
	return render(request, 'MainPage/about.html')

def food_items(request, FoodID):
	pass

def drink_items(request, DrinkID):
	pass
	
def searchFood(request):
	foods = Food.objects.all()
	context = {"foods": foods}
	return render(request, 'MainPage/foodlist.html', context)
	
def search_drink(request):
	drink_list = Drink.objects.all()
	paginator = Paginator(drink_list, 10)
	page = request.GET.get('page')
	try:
		drinks = paginator.page(page)
	except PageNotAnInteger:
		drinks = paginator.page(1)
	except EmptyPage:
		drinks = paginator.page(paginator.num_pages)
	return render(request, 'MainPage/drinklist.html', {'drinks':drinks})
	
	
	
def createFood(request):
	if request.method == 'POST':
		food = Food()
		food.name = request.POST.get("food_name")
		food.price = request.POST.get("food_price")
		food.description = request.POST.get("food_description")
		food.save()
		return HttpResponseRedirect('/success/')
	else:
		return render(request, 'MainPage/foodform.html')
		
def createDrink(request):
	if request.method == 'POST':
		drink = Drink()
		drink.name = request.POST.get("drink_name")
		drink.price = request.POST.get("drink_price")
		drink.description = request.POST.get("drink_description")
		drink.save()
		return HttpResponseRedirect('/success/')
	else:
		
		return render(request, 'MainPage/drinkform.html')
		
def order(request):
	return render(request, 'MainPage/order.html')
	
def request_waiter(request):
	return render(request, 'MainPage/waiter.html')
	
def success(request):
	return render(request, 'MainPage/success.html')