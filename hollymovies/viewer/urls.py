from django.urls import path

from .views import hello, movies, genres, MovieView, MovieDetailView, MovieCreateView, GenreCreateView, MovieUpdateView, \
    MovieDeleteView

urlpatterns = [
    path('hello/<s0>', hello),
    path('genres', genres, name='genres'),
    path('genres/new', GenreCreateView.as_view(), name='genre-create'),
    path('movies', MovieView.as_view(), name='movies'),
    path('movies/new', MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/edit', MovieUpdateView.as_view(), name='movie-update'),
    path('movies/<int:pk>/remove', MovieDeleteView.as_view(), name='movie-delete'),
    path('', movies, name='index'),
]
