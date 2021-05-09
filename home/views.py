from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def display(request):
	"""
    This method is used to display the home page
    
    :param request: it's a HttpResponse from user.
    
    :type request: HttpResponse.
    
    :return: this method returns a html page. It returns the home page where the user can navigate to different pages. 
    
    :rtype: HttpResponse.
    """
	return render(request, 'home.html')
