from django.urls import path
from chat.views import ChatListView, chat_create_view

app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view(), name='all'),
    path('new/', chat_create_view, name='new'),
]
