from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, CustomPasswordChangeView, SignUpView

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('password-change', CustomPasswordChangeView.as_view(), name='password-change'),
    path('sign-up', SignUpView.as_view(), name='sign-up')
]
