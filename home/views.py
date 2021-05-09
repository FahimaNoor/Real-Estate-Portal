from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def display(request):
	return render(request, 'home.html')
