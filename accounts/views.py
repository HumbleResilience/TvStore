from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm




class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ManageAccountView(TemplateView):
    template_name = 'registration/manage_account.html'

class PasswordChangePageView(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy('manage')
    template_name = "registration/change-password.html"
