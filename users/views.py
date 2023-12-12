from django.shortcuts import render, redirect, HttpResponseRedirect
from users.models import User
from users.forms import UserLoginForm
from django.contrib import auth, messages
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


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
            messages.success(request, 'Congratulations! Your registration was successful.')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print("Form is invalid", form.errors)
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/registration.html', context)


def profile(request):
    if request.method == "POST":
        form =UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': "Store - Profile", 'form': form}
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
