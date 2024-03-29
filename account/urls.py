from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),  #comment this line if you create different login app
    path("logout/", views.logout, name="logout"),
]
