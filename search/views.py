from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def search(request):
	"""
    This method helps to search.
    
    :param request: it's a HttpResponse from user.
    
    :type request: HttpResponse.
    
    :return: this method returns a html page. It returns the search html
    
    :rtype: HttpResponse.
    """
	return render(request, 'search.html')