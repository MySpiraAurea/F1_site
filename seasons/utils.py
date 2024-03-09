from .models import *

menu = [{'title': 'Личный зачет', 'url_name': 'drivers_standings'},
        {'title': 'Командный зачет', 'url_name': 'constructors_standings'},
        {'title': 'Новости', 'url_name': 'news'},
        {'title': 'Авторизация', 'url_name': 'login'},
        ]

sidebar = [{'title': 'Сезоны', 'function': 'seasons'},
           {'title': 'Гонщики', 'function': 'drivers'},
           {'title': 'Команды', 'function': 'teams'},
           {'title': 'Трассы', 'function': 'tracks'},
           {'title': 'Истории', 'function': 'stories'},
           ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['sidebar'] = sidebar
        return context

