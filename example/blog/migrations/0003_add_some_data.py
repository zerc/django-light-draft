# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

import random

from ..utils import saved, get_text


class Migration(DataMigration):

    def forwards(self, orm):
        # First - create some categories
        categories = saved(
            orm.Category(title=title)
            for title in ('Fan', 'Porno', 'Other'))

        # Now create some posts
        posts = saved(
            orm.BlogPost(
                title=get_text(2),
                lead=get_text(10),
                body=get_text(100),
                category=random.choice(categories)
            ) for x in xrange(5)
        )

        for x in xrange(3):
            orm.TextBlock(
                title=get_text(1),
                body=get_text(50),
                blog_post=posts[-1]
            ).save()

    def backwards(self, orm):
        orm.TextBlock.all().delete()
        orm.BlogPost.all().delete()
        orm.Category.all().delete()

    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'blog_posts'", 'null': 'True', 'to': u"orm['blog.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
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
