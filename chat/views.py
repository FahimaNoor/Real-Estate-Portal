from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from chat.forms import ChatForm
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import Chat
from django.utils import timezone


def chat_create_view(request):
    """
        This method is used to display the page of chat box where a user can write message.
        :param request: it's a HttpResponse from user.
        :type request: HttpResponse.
        :return: this method returns a chat box for chatting service which is a HTML page.
        :rtype: HttpResponse.
    """
    if request.method == 'POST':
        chat_form = ChatForm(request.POST)
        if chat_form.is_valid():
            chat_form.user = request.user
            chat_form.save()
            return redirect('chat:all')
        else:
            messages.error(request, 'Error Occurred')
    chat_form = ChatForm()
    return render(request=request, template_name="chat/chat_form.html", context={'chat_form': chat_form})


class ChatListView(LoginRequiredMixin, ListView):
    """
        This method is used to display chat page.
        :param request: it's a HttpResponse from user.
        :type request: HttpResponse.
        :return: this method returns a chat page for user which is a HTML page.
        :rtype: HttpResponse.
    """
    model = Chat

    def get_queryset(self):
        return Chat.objects.filter(posted_at__lte=timezone.now()).order_by('posted_at')
