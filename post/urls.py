from django.urls import path
from post.views import post_view, save_apartment_view

app_name = 'post'

urlpatterns = [
    path('postapartment', post_view, name='post_apartment'),
    path('saveapartment', save_apartment_view, name='save_apartment'),
]
