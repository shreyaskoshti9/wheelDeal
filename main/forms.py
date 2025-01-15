from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Vehicle, User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['title', 'make', 'model', 'year', 'condition', 'status', 'price', 'description', 'image']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
