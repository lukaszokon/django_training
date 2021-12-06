from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView

from .forms import CustomPasswordChangeForm


class CustomLoginView(LoginView):
    template_name = 'forms.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('movies')
    form_class = CustomPasswordChangeForm
