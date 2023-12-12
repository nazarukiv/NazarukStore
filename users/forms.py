from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Enter your username'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class': 'form-control py-4', 'placeholder': 'Enter your password'}))
    class Meta:
       model = User
       fields = ('username', 'password')




class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Enter your last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Enter your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={  # Use forms.EmailField here
        'class': 'form-control py-4',
        'placeholder': 'Enter your email address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Confirm your password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
