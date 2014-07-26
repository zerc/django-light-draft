# coding: utf-8
from __future__ import unicode_literals

from light_draft.views import BaseDraftView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'posts'


class BlogPostDetailView(BaseDraftView):
    model = BlogPost
    context_object_name = 'post'
