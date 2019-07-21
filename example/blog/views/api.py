# coding: utf-8
from __future__ import unicode_literals

from rest_framework import routers, serializers, viewsets
from blog.models import BlogPost, Category, Tag, TextBlock

from light_draft.views import DraftAPIViewMixin


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'colour_class']


class TextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBlock
        fields = ['title', 'body']


class BlogPostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    blocks = TextBlockSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = BlogPost
        fields = ['pk', 'title', 'lead', 'body', 'category', 'tags', 'blocks']


class BlogPostViewSet(DraftAPIViewMixin, viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
