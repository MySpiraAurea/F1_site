from django.contrib import admin
from .models import *


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)
    list_editable = ('is_published',)
    list_filter = ('title', 'time_create',)
    prepopulated_fields = {'slug': ('title',)}


class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'team_name', 'is_driving', 'is_published')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'content',)
    list_editable = ('is_published', 'is_driving',)
    list_filter = ('name', 'is_driving',)
    prepopulated_fields = {'slug': ('name',)}


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'is_existing', 'is_published',)
    list_display_links = ('id', 'team',)
    search_fields = ('team', 'content', 'drivers',)
    list_editable = ('is_published', 'is_existing',)
    list_filter = ('team', 'is_existing',)
    prepopulated_fields = {'slug': ('team',)}


class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'in_calendar', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content', 'country')
    list_editable = ('in_calendar', 'is_published',)
    list_filter = ('name', 'in_calendar')
    prepopulated_fields = {'slug': ('name',)}


class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('title', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('title', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Driver, DriverAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(News, NewsAdmin)
