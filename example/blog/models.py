# coding: utf-8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class BlogPost(models.Model):
    title = models.CharField('title', max_length=255)

    lead = models.TextField('lead')
    body = models.TextField('body')

    class Meta:
        verbose_name = 'blog post'
        verbose_name_plural = 'blog posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'pk': self.pk})
