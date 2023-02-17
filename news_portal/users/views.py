from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import RegistrationForm
from django.urls import reverse_lazy


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

    def get_queryset(self):
        return super(Account, self).get_queryset().filter(id=self.request.user.id)


class Account_Update(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email')
    template_name = 'users/user_form_update.html'

    def get_success_url(self):
        return reverse_lazy('account', kwargs={'pk': self.kwargs['pk']})

    def get_queryset(self):
        return super(Account, self).get_queryset().filter(id=self.request.user.id)
