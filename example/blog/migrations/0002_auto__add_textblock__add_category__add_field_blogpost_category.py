# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TextBlock'
        db.create_table(u'blog_textblock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog_post', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'blocks', to=orm['blog.BlogPost'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'blog', ['TextBlock'])

        # Adding model 'Category'
        db.create_table(u'blog_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'blog', ['Category'])

        # Adding field 'BlogPost.category'
        db.add_column(u'blog_blogpost', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'blog_posts', null=True, to=orm['blog.Category']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'TextBlock'
        db.delete_table(u'blog_textblock')

        # Deleting model 'Category'
        db.delete_table(u'blog_category')

        # Deleting field 'BlogPost.category'
        db.delete_column(u'blog_blogpost', 'category_id')


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