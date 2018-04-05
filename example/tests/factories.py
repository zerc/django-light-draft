# coding: utf-8
from __future__ import unicode_literals

import factory
from django.contrib.auth import get_user_model

from blog import models

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tag


class BlogPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BlogPost

    category = factory.SubFactory(CategoryFactory)
    body = factory.Sequence(lambda n: 'Body body#{}'.format(n))
    lead = factory.Sequence(lambda n: 'Lead lead#{}'.format(n))

    @factory.post_generation
    def tags_count(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        tags = TagFactory.create_batch(extracted)
        self.tags.add(*tags)

    @factory.post_generation
    def blocks_count(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        TextBlockFactory.create_batch(extracted, blog_post=self)

class TextBlockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TextBlock

    blog_post = factory.SubFactory(BlogPostFactory)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    is_active = True
    is_staff = True
    is_superuser = True
