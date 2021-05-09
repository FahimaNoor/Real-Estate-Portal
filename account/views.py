from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as logouts

def register(request):
	"""
    This method is used to show the selection page of see available ICU and see available hospital bed.
    by clicking one of the option it shows the corresponding page.
    
    :param request: it's a HttpResponse from user.
    
    :type request: HttpResponse.
    
    :return: this method returns a html page.It returns a page where it has two options.one is see available
    ICU and see available hospital base pages.
    
    :rtype: HttpResponse.
    """
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request,'register.html', {'form': form})


def login(request):
	"""
    This method is used to show the selection page of see available ICU and see available hospital bed.
    by clicking one of the option it shows the corresponding page.
    
    :param request: it's a HttpResponse from user.
    
    :type request: HttpResponse.
    
    :return: this method returns a html page. It returns the login form for the user to login. After sucessful login, the user is redirected to home page.
    
    :rtype: HttpResponse.
    """
	if request.method == 'POST':
		form = AuthenticationForm(data= request.POST)
		if form.is_valid():
			return redirect('display')
	else:
		form = AuthenticationForm()
	return render(request,'login.html', {'form': form})

def logout(request):
	"""
    This method Logs out the user.
    
    :param request: it's a HttpResponse from user.
    
    :type request: HttpResponse.
    
    :return: this method returns a html page.It returns the logout html
    
    :rtype: HttpResponse.
    """
	if request.method == 'POST':
		auth.logout(request)
		return render(request,"logout")





