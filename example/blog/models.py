# coding: utf-8
from __future__ import unicode_literals
import random

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField('title', max_length=255)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Tag(models.Model):
    title = models.CharField('title', max_length=255)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.title

    @property
    def colour_class(self):
        """Return a random CSS class for the tag."""
        choices = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'dark']
        return random.choice(choices)

@python_2_unicode_compatible
class BlogPost(models.Model):
    title = models.CharField('title', max_length=255)

    lead = models.TextField('lead')
    body = models.TextField('body')

    category = models.ForeignKey(
        Category, related_name='blog_posts', blank=True, null=True, on_delete=models.PROTECT)

    tags = models.ManyToManyField(Tag, related_name='blog_post')

    class Meta:
        verbose_name = 'blog post'
        verbose_name_plural = 'blog posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'pk': self.pk})


@python_2_unicode_compatible
class TextBlock(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='blocks', on_delete=models.PROTECT)

    title = models.CharField('title', max_length=255)
    body = models.TextField('body')

    class Meta:
        verbose_name = 'text block'
        verbose_name_plural = 'text blocks'

    def __str__(self):
        return self.title
