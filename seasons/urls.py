from django.urls import path
from .views import *

urlpatterns = [
    path('', FormulaHome.as_view(), name='home'),
    path('seasons/', Seasons.as_view(), name='seasons'),
    path('seasons/<slug:season_slug>/', ShowSeason.as_view(), name='season_number'),
    path('teams/', Teams.as_view(), name='teams'),
    path('teams/<slug:team_slug>/', ShowTeam.as_view(), name='team_name'),
    path('drivers/', Drivers.as_view(), name='drivers'),
    path('drivers/<slug:driver_slug>/', ShowDriver.as_view(), name='driver_name'),
    path('tracks/', Tracks.as_view(), name='tracks'),
    path('tracks/<slug:track_slug>/', ShowTrack.as_view(), name='show_track'),
    path('stories/', Stories.as_view(), name='stories'),
    path('stories/<slug:story_slug>/', ShowStory.as_view(), name='show_story'),
    path('news/', NewsPage.as_view(), name='news'),
    path('news/<slug:news_slug>/', ShowNews.as_view(), name='show_news'),
    path('drivers_standings/', drivers_standings, name='drivers_standings'),
    path('constructors_standings/', constructors_standings, name='constructors_standings'),
    path('login/', login, name='login'),
]