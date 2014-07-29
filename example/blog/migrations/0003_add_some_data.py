# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

import random

saved = lambda seq: [s for s in seq if s.save() is None]


text = """
    Return a k length list of unique elements chosen from the
    population sequence. Used for random sampling without replacement.
    New in version 2.3.
    Returns a new list containing elements from the population
    while leaving the original population unchanged. The resulting
    list is in selection order so that all sub-slices will also be
    valid random samples. This allows raffle winners (the sample)
    to be partitioned into grand prize and second place winners
    (the subslices).
    Members of the population need not be hashable or unique.
    If the population contains repeats, then each occurrence is a
    possible selection in the sample.
    To choose a sample from a range of integers, use an
    xrange() object as an argument. This is especially fast
    and space efficient for sampling from a large population:
    sample(xrange(10000000), 60).
    """


get_text = lambda num: ' '.join(random.sample(text.split(), num))


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
