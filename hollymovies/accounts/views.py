import django.contrib.auth.models
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import CustomPasswordChangeForm, SignUpForm, CustomAdminPasswordChangeForm, CustomUserChangeForm
from .models import Profile


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class UserListView(PermissionRequiredMixin, ListView):
    template_name = 'users.html'
    model = Profile
    context_object_name = 'profiles'
    permission_required = 'accounts.add_profile'


class ProfileDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'profile_delete.html'
    model = Profile
    success_url = reverse_lazy('user-list')
    permission_required = 'accounts.delete_profile'


class ProfileUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'forms.html'
    form_class = CustomUserChangeForm
    model = django.contrib.auth.models.User
    success_url = reverse_lazy('user-list')
    permission_required = 'accounts.change_profile'

    def get_object(self, queryset=None):
        return Profile.objects.get(pk=self.kwargs['pk']).user


class SignUpView(CreateView):
    template_name = 'forms.html'
    form_class = SignUpForm
    success_url = reverse_lazy('movies')


class CustomLoginView(LoginView):
    template_name = 'forms.html'


class CustomAdminPasswordChangeView(PermissionRequiredMixin,
                                    PasswordChangeView):
    template_name = 'admin_password_change.html'
    success_url = reverse_lazy('user-list')
    form_class = CustomAdminPasswordChangeForm
    permission_required = 'accounts.change_profile'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = Profile.objects.get(pk=self.kwargs['pk']).user
        return kwargs


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
