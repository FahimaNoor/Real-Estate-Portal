from django.shortcuts import render, redirect
from django.http import HttpResponse
from post.forms import PostForm, ApartmentForm
from django.contrib import messages


# Post functionality
def post_view(request):
    """
       This method is used to display post functionality.
       :param request: it's a HttpResponse from user.
       :type request: HttpResponse.
       :return: this method returns a post form for post page which is a HTML page.
       :rtype: HttpResponse.
    """
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.user = request.user
            post_form.save()
            messages.success(request, "Information Saved")
            return redirect('home')
        else:
            messages.error(request, "Error Occurred")
    post_form = PostForm()
    return render(request=request, template_name='post/post.html', context={'post_form': post_form})


# Save Apartment functionality
def save_apartment_view(request):
    """
       This method is used for saving apartments details.
       :param request: it's a HttpResponse from user.
       :type request: HttpResponse.
       :return: this method returns a saving apartment form which is a HTML page.
       :rtype: HttpResponse.
    """
    if request.method == 'POST':
        save_apartment_form = ApartmentForm(request.POST)
        if save_apartment_form.is_valid():
            save_apartment_form.save()
            messages.success(request, "Information Saved")
            return redirect('home')
        else:
            messages.error(request, "Error Occurred")
    save_apartment_form = ApartmentForm()
    return render(request=request, template_name='post/saveapartment.html', context={'save_apartment_form': save_apartment_form})
