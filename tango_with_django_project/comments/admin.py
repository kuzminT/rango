# coding: utf-8
from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',
                    'text')


admin.site.register(Comment, CommentAdmin)

