from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import authenticationform

# Create your views here.

def login(request):
	if request.method == 'POST':
		form = authentication_form(data= request.POST)
		if form.is_valid():
			return redirect('display')
	else:
		form = authentication_form()
	return render(request,'login.html', {'form': form})