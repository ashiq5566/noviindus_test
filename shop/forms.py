from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Re-password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'company_name', 'product_image', 'description', 'price', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'name'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'company name'}),
            'product_image': forms.FileInput(attrs={'class': 'form-control my-2', 'required': 'true'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-2', 'placeholder': 'description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control my-2', 'placeholder': 'price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control my-2', 'placeholder': 'quantity'}),
        }


