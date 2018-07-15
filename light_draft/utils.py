# coding: utf-8
from __future__ import unicode_literals

import os

try:
    import cPickle as pickle
except ImportError:
    import pickle

from uuid import uuid4

from django.db.models.fields.related import RelatedField
from django.forms.models import model_to_dict
from django.core.cache import caches

from .settings import DRAFT_TMP_DIR, DRAFT_SETTINGS
from .exceptions import CacheMissError


def make_cache_key(instance):
    """Construct a cache key for the instance."""
    prefix = '{}:{}:{}'.format(
        instance._meta.app_label,
        instance._meta.model_name,
        instance.pk
    )
    return '{}:{}'.format(prefix, str(uuid4()))


def save_model_snapshot(instance, related_objects=None):
    """Serialize the instance given."""
    key = make_cache_key(instance)
    data = {'instance': instance, 'related_objects': related_objects}
    cache = caches[DRAFT_SETTINGS['cache_name']]
    cache.set(key, pickle.dumps(data), DRAFT_SETTINGS['ttl'])
    return key


def load_from_shapshot(model, key):
    """
    Load data from the snapshot stored.

    If the value is not in cache then fallback to the old (file-based) method.
    """
    # New way of doing things
    if key.startswith(model._meta.app_label):
        cache = caches[DRAFT_SETTINGS['cache_name']]
        try:
            data = pickle.loads(cache.get(key))
        except TypeError:
            raise CacheMissError(key)
    # Old way. Deprecated.
    else:
        data = _get_data_old(model, key)

    instance = data.pop('instance')
    instance._prefetched_objects_cache = data.pop('related_objects')
    return instance


def _get_data_old(model, key):
    """DEPERECATED."""
    path = os.path.join(
        DRAFT_TMP_DIR,
        model._meta.app_label,
        model._meta.model_name,
        key
    )

    try:
        with open(path, 'rb') as f:
            return pickle.load(f)
    except IOError:
        raise CacheMissError(path)
