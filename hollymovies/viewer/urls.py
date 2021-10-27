from django.urls import path

from .views import hello, movies

urlpatterns = [
    path('hello/<s0>', hello),
    path('', movies, name='index')
]
