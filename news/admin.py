from django.contrib import admin

from news.models import Type, News


@admin.register(Type)
class WidgetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'color']
    search_fields = ['id', 'name']


@admin.register(News)
class WidgetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_desc', 'type']
    search_fields = ['id', 'name']
    list_filter = ['type']
