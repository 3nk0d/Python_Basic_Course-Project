from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import RegistrationForm


# Create your views here.

class Registration_View(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'users/user_form.html'


class Login_View(LoginView):
    model = User
    template_name = 'users/login.html'


class Logout_View(LogoutView):
    model = User
    template_name = 'users/logout.html'


class Account(DetailView):
    model = User
    template_name = 'users/account.html'
