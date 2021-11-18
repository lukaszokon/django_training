from logging import getLogger
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .forms import MovieForm
from .models import Movie, Genre

LOGGER = getLogger()


class CustomLoginView(LoginView):
    template_name = 'forms.html'


class GenreCreateView(LoginRequiredMixin, CreateView):
    model = Genre
    fields = '__all__'
    template_name = 'forms.html'
    success_url = reverse_lazy('genres')


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genre_detail.html'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(genre=self.get_object())
        return context


class GenreUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'forms.html'
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('genres')


class GenreDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'genre_delete.html'
    model = Genre
    success_url = reverse_lazy('genres')


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'movie_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')


class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'movie_form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movies')

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'


class MovieView(ListView):
    template_name = 'movies.html'
    model = Movie
    context_object_name = 'movies'


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(request, template_name='hello.html', context={'adjectives': [s0, s1, 'beautiful', 'wonderful']})


def movies(request):
    sorting = request.GET.get('s', 'default')
    if sorting == 'title':
        movies_list = Movie.objects.all().order_by('title')
    elif sorting == 'rating':
        movies_list = Movie.objects.all().order_by('-rating')
    elif sorting == 'year':
        movies_list = Movie.objects.all().order_by('released')
    else:
        movies_list = Movie.objects.all()

    return render(request, template_name='movies.html', context={'movies': movies_list})


def genres(request):
    return render(request, template_name='genres.html', context={'genres': Genre.objects.all()})
