from django import forms
from chat.models import Chat


# Chat Form
class ChatForm(forms.ModelForm):
    message = forms.CharField(required=True, widget=forms.TextInput())

    class Meta:
        model = Chat
        fields = ('message',)

    def save(self, commit=True):
        save_message = super(ChatForm, self).save(commit=False)
        save_message.user = self.user
        save_message.message = self.cleaned_data['message']

        if commit:
            save_message.save()
        return save_message
