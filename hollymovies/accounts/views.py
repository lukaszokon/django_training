from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import CustomPasswordChangeForm, SignUpForm
from .models import Profile


class UserListView(PermissionRequiredMixin, ListView):
    template_name = 'users.html'
    model = Profile
    context_object_name = 'profiles'
    permission_required = 'accounts.add_profile'


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


def change_user_active(request, pk):
    profile = Profile.objects.get(pk=pk)
    if profile.user.is_active:
        profile.user.is_active = False
    else:
        profile.user.is_active = True
    profile.user.save()
    return HttpResponseRedirect(reverse_lazy('user-list'))
