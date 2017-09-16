# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from rango.models import Category
from django.utils import timezone


class Comment(models.Model):

    title =  models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey(Category)
    created_date =  models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50, default='anonymous')

    def __uncicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Комментарии'


