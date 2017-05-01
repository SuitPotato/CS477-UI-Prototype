from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def splash(request):
	return render(request, 'Splash/splash.html')