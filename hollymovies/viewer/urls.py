from django.urls import path

from .views import hello, movies, genres

urlpatterns = [
    path('hello/<s0>', hello),
    path('genres', genres, name='genres'),
    path('', movies, name='index'),
]
