from django import template

sidebar = [{'title': 'Сезоны', 'function': 'seasons'},
           {'title': 'Гонщики', 'function': 'drivers'},
           {'title': 'Команды', 'function': 'teams'},
           {'title': 'Трассы', 'function': 'tracks'},
           {'title': 'Истории', 'function': 'stories'},
           ]

menu = [{'title': 'Личный зачет', 'url_name': 'drivers_standings'},
        {'title': 'Командный зачет', 'url_name': 'constructors_standings'},
        {'title': 'Новости', 'url_name': 'news'},
        {'title': 'Авторизация', 'url_name': 'login'},
        ]

register = template.Library()

@register.simple_tag()
def get_sidebar():
    return sidebar


@register.simple_tag()
def get_menu():
    return menu


@register.inclusion_tag('seasons/sidebar.html')
def show_sidebar(category=''):
    return {'sidebar': sidebar, 'category': category}

@register.inclusion_tag('seasons/mainmenu.html')
def show_mainmenu():
    return {'menu': menu}

