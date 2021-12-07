from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView, PasswordChangeView

from .forms import CustomPasswordChangeForm, SignUpForm
from .models import Profile


class UserListView(ListView):
    template_name = 'users.html'
    model = Profile
    context_object_name = 'profiles'

class SignUpView(CreateView):
    template_name = 'forms.html'
    form_class = SignUpForm
    success_url = reverse_lazy('movies')


class CustomLoginView(LoginView):
    template_name = 'forms.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('movies')
    form_class = CustomPasswordChangeForm
