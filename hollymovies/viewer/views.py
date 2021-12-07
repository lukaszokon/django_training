from logging import getLogger
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from .forms import MovieForm
from .models import Movie, Genre

LOGGER = getLogger()


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class GenreCreateView(StaffRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Genre
    fields = '__all__'
    template_name = 'forms.html'
    success_url = reverse_lazy('genres')
    permission_required = 'viewer.add_genre'


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


class MovieDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'movie_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.add_movie'

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'movie_form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.change_movie'

    def form_invalid(self, form):
        LOGGER.warning('User provided wrong data.')
        return super().form_invalid(form)


class MovieDetailView(PermissionRequiredMixin, DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'
    permission_required = 'viewer.view_movie'


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
