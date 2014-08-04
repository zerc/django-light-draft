# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

import random

from ..utils import saved, get_text

TAGS_TITLES = (
    'Advertising', 'Advice', 'Africa', 'Android', 'Anime',
    'Apple', 'Architecture', 'Art', 'Baking', 'Beauty', 'Bible',
    'Blog', 'Blogging', 'Book Reviews', 'Books', 'Branding',
    'Business', 'Canada', 'Cars', 'Cartoons', 'Celebrities',
    'Celebrity', 'Children', 'Christian', 'Christianity',
    'Comedy', 'Comics', 'Cooking', 'Cosmetics', 'Crafts',
    'Cuisine', 'Culinary', 'Culture', 'Dating', 'Design',
    'Diy', 'Dogs', 'Drawing', 'Economy', 'Education',
    'Entertainment', 'Environment', 'Events', 'Exercise',
    'Faith', 'Family', 'Fantasy', 'Porn'
)

TAGS_COUNT = len(TAGS_TITLES)


class Migration(DataMigration):

    def forwards(self, orm):
        tags = saved(orm.Tag(title=title) for title in TAGS_TITLES)

        for post in orm.BlogPost.objects.all():
            post.tags.add(
                *random.sample(tags, random.randint(0, TAGS_COUNT-1)))

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'blog_posts'", 'null': 'True', 'to': u"orm['blog.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'blog_post'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['blog.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.textblock': {
            'Meta': {'object_name': 'TextBlock'},
            'blog_post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'blocks'", 'to': u"orm['blog.BlogPost']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']
    symmetrical = True
