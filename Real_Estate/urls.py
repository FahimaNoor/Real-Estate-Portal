"""Real_Estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from Real_Estate.views import HomePage

urlpatterns = [
    # admin page
    path('admin/', admin.site.urls),
    # index page
    path('', HomePage.as_view(), name='home'),
    # Post functionality
    url('post/', include('post.urls'), name='post'),
    # User functionality
    url('accounts/', include('user.urls'), name='user'),
    # Chat functionality
    url('chat/', include('chat.urls'), name='chat'),
]
