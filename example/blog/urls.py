# coding: utf-8
from django.conf.urls import url

from .views import BlogPostListView, BlogPostDetailView


urlpatterns = [
    url(r'^$', BlogPostListView.as_view(), name='posts_list'),
    url(r'^(?P<pk>\d+)$', BlogPostDetailView.as_view(), name='blog_post_detail'),
]
