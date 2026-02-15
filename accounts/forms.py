from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ApplicantProfile

class ApplicantRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="Ism", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}))
    last_name = forms.CharField(label="Familiya", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangiz'}))
    email = forms.EmailField(label="Elektron pochta", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}))
    password1 = forms.CharField(label="Parol", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol kiriting'}))
    password2 = forms.CharField(label="Parolni tasdiqlang", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni qayta kiriting'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {'username': 'Foydalanuvchi nomi'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomi'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Foydalanuvchi nomi", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomi'}))
    password = forms.CharField(label="Parol", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'}))

class ApplicantProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Ism", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Familiya", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Elektron pochta", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ApplicantProfile
        fields = ['otasining_ismi', 'tugilgan_sana', 'telefon', 'manzil', 'passport_seriya', 'rasm']
        widgets = {
            'otasining_ismi': forms.TextInput(attrs={'class': 'form-control'}),
            'tugilgan_sana': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+998 XX XXX XX XX'}),
            'manzil': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'passport_seriya': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AA 1234567'}),
            'rasm': forms.FileInput(attrs={'class': 'form-control'}),
        }
