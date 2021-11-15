from django.urls import path

from .views import hello, movies, genres, MovieView, MovieDetailView, MovieCreateView

urlpatterns = [
    path('hello/<s0>', hello),
    path('genres', genres, name='genres'),
    path('movies', MovieView.as_view(), name='movies'),
    path('movies/new', MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('', movies, name='index'),
]
