# coding: utf-8
from django.conf.urls import url, include
from rest_framework import routers

from blog.views.views import BlogPostListView, BlogPostDetailView
from blog.views import api

router = routers.DefaultRouter()
router.register('blog-posts', api.BlogPostViewSet)

urlpatterns = [
    url(r'^$', BlogPostListView.as_view(), name='posts_list'),
    url(r'^(?P<pk>\d+)$', BlogPostDetailView.as_view(), name='blog_post_detail'),
    url(r'^api-auth/', include('rest_framework.urls'))
]
