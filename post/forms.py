from django import forms
from post.models import PostModel, ApartmentModel


# Apartment Details Form
class ApartmentForm(forms.ModelForm):
    location = forms.CharField(required=True, widget=forms.TextInput())
    apartment_type = forms.CharField(required=True, widget=forms.TextInput())
    description = forms.CharField(required=True, widget=forms.TextInput())
    utilities = forms.CharField(required=True, widget=forms.TextInput())
    picture = forms.ImageField(required=False)
    money = forms.IntegerField(required=True, widget=forms.NumberInput())

    class Meta:
        model = ApartmentModel
        fields = ('location', 'apartment_type', 'description', 'utilities', 'picture', 'money')

    def save(self, commit=True):
        save_apartment = super(ApartmentForm, self).save(commit=False)
        save_apartment.location = self.cleaned_data['location']
        save_apartment.apartment_type = self.cleaned_data['apartment_type']
        save_apartment.description = self.cleaned_data['description']
        save_apartment.utilities = self.cleaned_data['utilities']
        save_apartment.picture = self.cleaned_data['picture']
        save_apartment.money = self.cleaned_data['money']

        if commit:
            save_apartment.save()
        return save_apartment


# Post Form
class PostForm(forms.ModelForm):
    post_header = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'input100', 'placeholder': 'Enter your Post Header:'
        }), label='Header')

    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'input100', 'placeholder': 'Enter your Phone Number:'
    }), label='Phone')

    apartment_id = forms.ModelChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'dropdown-item',
    }), queryset=ApartmentModel.objects.all(), label='Select Apartment')

    type_choice = (('---', '--------'), ('Sell', 'Sell'), ('Rent', 'Rent'))
    is_sell_post = forms.ChoiceField(required=True, choices=type_choice, widget=forms.Select(attrs={
        'class': 'dropdown-item',
    }), label='Select Post Type:')

    class Meta:
        model = PostModel
        fields = ('post_header', 'phone', 'apartment_id', 'is_sell_post')

    def save(self, commit=True):
        save_post = super(PostForm, self).save(commit=False)
        save_post.post_header = self.cleaned_data['post_header']
        save_post.email = self.user
        save_post.phone = self.cleaned_data['phone']
        save_post.apartment_id = self.cleaned_data['apartment_id']
        save_post.is_sell_post = self.cleaned_data['is_sell_post']
        if commit:
            save_post.save()
        return save_post
