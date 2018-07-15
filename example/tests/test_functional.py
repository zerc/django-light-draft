# coding: utf-8
"""Functional tests."""
from __future__ import unicode_literals
import re

from django.test import TestCase
from django.utils.encoding import force_text
from parameterized import parameterized

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from tests import factories as f


class DraftLogicTestCase(TestCase):
    """TestCase for the whole logic serialisation / deserialisation."""

    @classmethod
    def setUpClass(cls):
        super(DraftLogicTestCase, cls).setUpClass()
        cls.post = f.BlogPostFactory(tags_count=2, blocks_count=2)
        cls.admin_change_url = reverse('admin:blog_blogpost_change', args=(cls.post.pk,))
        cls.admin_preview_url = reverse('admin:blog_blogpost_preview', args=(cls.post.pk,))
        cls.admin_user = f.UserFactory(username='admin')
        cls.admin_user.set_password('admin')
        cls.admin_user.save()

    def setUp(self):
        super(DraftLogicTestCase, self).setUp()
        # Use `client.force_login` only after removing support of Django 1.8.x
        if hasattr(self.client, 'force_login'):
            self.client.force_login(self.admin_user)
        else:
            self.client.login(username='admin', password='admin')

    def test_everything(self):
        """Check that everything works."""
        response = self.client.get(self.admin_change_url)
        self.assertEqual(response.status_code, 200)

        block_0, block_1 = self.post.blocks.all()

        post_data = {
            'blocks-0-blog_post': self.post.pk,
            'blocks-0-body': block_0.body,
            'blocks-0-id': block_0.pk,
            'blocks-0-title': block_0.title,
            'blocks-1-blog_post': self.post.pk,
            'blocks-1-body': block_1.body,
            'blocks-1-id': block_1.pk,
            'blocks-1-title': block_1.title,
            'blocks-2-blog_post': self.post.pk,
            'blocks-2-body': '',
            'blocks-2-id': '',
            'blocks-2-title': '',
            'blocks-3-blog_post': '10',
            'blocks-3-body': '',
            'blocks-3-id': '',
            'blocks-3-title': '',
            'blocks-INITIAL_FORMS': '2',
            'blocks-MAX_NUM_FORMS': '1000',
            'blocks-MIN_NUM_FORMS': '0',
            'blocks-TOTAL_FORMS': '4',
            'blocks-__prefix__-blog_post': self.post.pk,
            'blocks-__prefix__-body': '',
            'blocks-__prefix__-id': '',
            'blocks-__prefix__-title': '',
            'body': self.post.body,
            'category': self.post.category_id,
            'lead': self.post.lead,
            'tags': [t.pk for t in self.post.tags.all()],
            'title': 'Hello',
        }
        response = self.client.post(self.admin_preview_url, post_data)
        self.assertEqual(response.status_code, 200)

        url = force_text(response.content)

        self.assertTrue(url.startswith(
            '{url}?hash=blog:blogpost:{pk}'.format(
                url=self.post.get_absolute_url(),
                pk=self.post.pk
            )), url
        )

        # Changes are on the page
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(re.findall('<h1>\s+Hello\n', force_text(response.content)))

        # But not in the database
        post = type(self.post).objects.get(pk=self.post.pk)
        self.assertNotEqual(post.title, 'Hello')

    @parameterized.expand([
        ('something',),  # old key
        ('blog:blogpost:1:something',)
    ])
    def test_cache_miss(self, key):
        """Check the case when the cache key does not exist."""
        url = '{}?hash={}'.format(self.post.get_absolute_url(), key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
