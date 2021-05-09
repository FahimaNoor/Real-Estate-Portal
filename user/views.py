from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.forms import RegistrationForm, LoginForm
from django.http import HttpResponse


# Login functionality
def login_view(request):
    """
       This method is used for user login.
       :param request: it's a HttpResponse from user.
       :type request: HttpResponse.
       :return: this method returns login form which is a HTML page.
       :rtype: HttpResponse.
    """
    if request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    login_form = LoginForm()
    return render(request=request, template_name="user/login.html", context={"login_form": login_form})


# Register Functionality
def register_view(request):
    """
       This method is used for user registration.
       :param request: it's a HttpResponse from user.
       :type request: HttpResponse.
       :return: this method returns registration form which is a HTML page.
       :rtype: HttpResponse.
    """
    if request.method == 'POST':
        register_form = RegistrationForm(request, data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    register_form = RegistrationForm()
    return render(request=request, template_name='user/register.html', context={'register_form': register_form})


# Logout Functionality
@login_required
def logout_view(request):
    """
       This method is used for user logout.
       :param request: it's a HttpResponse from user.
       :type request: HttpResponse.
       :return: this method returns logout which is a HTML page.
       :rtype: HttpResponse.
    """
    logout(request)
    return redirect('home')
