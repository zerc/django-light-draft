# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin
from light_draft.admin import DraftAdmin

from .models import BlogPost


class BlogPostAdmin(DraftAdmin):
    list_display = ('pk', 'title')
    fields = ('title', 'lead', 'body')


admin.site.register(BlogPost, BlogPostAdmin)
