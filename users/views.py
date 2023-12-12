from django.shortcuts import render, redirect, HttpResponseRedirect
from users.models import User
from users.forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
#Authorization of user by checking 3 steps:Audit, Authentication, Authorization

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  #cleaned_data to get form field values
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))

    if request.method == "GET":
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)

from django.shortcuts import render, HttpResponseRedirect, reverse

def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        print("Reached post request handling")
        if form.is_valid():
            print("Form is valid")
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print("Form is invalid", form.errors)
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/registration.html', context)
