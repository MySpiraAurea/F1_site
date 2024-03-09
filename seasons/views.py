from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView
from .utils import *

menu = [{'title': 'Личный зачет', 'url_name': 'drivers_standings'},
        {'title': 'Командный зачет', 'url_name': 'constructors_standings'},
        {'title': 'Новости', 'url_name': 'news'},
        {'title': 'Авторизация', 'url_name': 'login'},
        ]


# Create your views here.
class FormulaHome(DataMixin, ListView):
    model = News
    template_name = 'seasons/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Season.objects.filter(is_published=True)


class Seasons(ListView):
    model = Season
    template_name = 'seasons/seasons.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Сезоны'
        context['category'] = 'seasons'
        return context

    def get_queryset(self):
        return Season.objects.filter(is_published=True)


class ShowSeason(DetailView):
    model = Season
    template_name = 'seasons/show_season.html'
    slug_url_kwarg = 'season_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        context['category'] = 'seasons'
        return context


class Drivers(ListView):
    model = Driver
    template_name = 'seasons/drivers.html'
    context_object_name = 'drivers'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Гонщики'
        context['category'] = 'drivers'
        return context

    def get_queryset(self):
        return Driver.objects.filter(is_published=True)


class ShowDriver(DetailView):
    model = Driver
    template_name = 'seasons/show_driver.html'
    slug_url_kwarg = 'driver_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        context['category'] = 'drivers'
        return context


class Teams(ListView):
    model = Team
    template_name = 'seasons/teams.html'
    context_object_name = 'teams'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Команды'
        context['category'] = 'teams'
        return context

    def get_queryset(self):
        return Team.objects.filter(is_published=True)


class ShowTeam(DetailView):
    model = Team
    template_name = 'seasons/show_team.html'
    slug_url_kwarg = 'team_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        context['category'] = 'teams'
        return context


class Tracks(ListView):
    model = Track
    template_name = 'seasons/tracks.html'
    context_object_name = 'tracks'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Трассы'
        context['category'] = 'tracks'
        return context

    def get_queryset(self):
        return Track.objects.filter(is_published=True)


class ShowTrack(DetailView):
    model = Track
    template_name = 'seasons/show_track.html'
    slug_url_kwarg = 'track_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        context['category'] = 'tracks'
        return context

class Stories(ListView):
    model = Story
    template_name = 'seasons/stories.html'
    context_object_name = 'stories'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Истории'
        context['category'] = 'stories'
        return context

    def get_queryset(self):
        return Story.objects.filter(is_published=True)


class ShowStory(DetailView):
    model = Story
    template_name = 'seasons/show_story.html'
    slug_url_kwarg = 'story_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        context['category'] = 'stories'
        return context


class NewsPage(ListView):
    model = News
    template_name = 'seasons/news.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Новости'
        context['category'] = 'news'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class ShowNews(DetailView):
    model = News
    template_name = 'seasons/show_news.html'
    slug_url_kwarg = 'news_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        context['category'] = 'news'
        return context


def drivers_standings(request):
    return HttpResponse('зачет пилотов')


def constructors_standings(request):
    return HttpResponse('зачет команд')


def login(request):
    return HttpResponse('Регистрация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

