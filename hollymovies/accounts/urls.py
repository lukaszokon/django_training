from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, CustomPasswordChangeView, CustomAdminPasswordChangeView, SignUpView, UserListView, ProfileDeleteView, \
    change_user_active

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('password-change', CustomPasswordChangeView.as_view(), name='password-change'),
    path('sign-up', SignUpView.as_view(), name='sign-up'),
    path('users', UserListView.as_view(), name='user-list'),
    path('<int:pk>/delete', ProfileDeleteView.as_view(), name='user-delete'),
    path('<int:pk>/change-password', CustomAdminPasswordChangeView.as_view(), name='user-change-password'),
    path('<int:pk>/change-user-active', change_user_active, name='change-user-active')
]
