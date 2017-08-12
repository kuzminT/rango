# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',
                    'url')
    # Можно указать, какие поля будут являться атрибутами модели
    # list_display_links = ('title', 'category', 'url')
    # Можно перечислить поля, доступные для редактирования на странице списка.
    # list_editable = ('category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)