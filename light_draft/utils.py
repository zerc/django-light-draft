# coding: utf-8
from __future__ import unicode_literals

import os
import cPickle as pickle
from uuid import uuid4

from django.db.models.fields.related import RelatedField
from django.forms.models import model_to_dict

from .settings import DRAFT_TMP_DIR


def save_model_snapshot(instance, related_objects=None):
    """
    Serialize instance into .pickle cache file
    """
    parts = (
        DRAFT_TMP_DIR,
        instance._meta.app_label,
        instance._meta.model_name
    )

    # Create all necessary dirs
    prev = ''
    for part in parts:
        path = os.path.join(prev, part)
        if not os.path.exists(path):
            os.mkdir(path)
        prev = path

    file_hash = str(uuid4())

    data = {'instance': instance, 'related_objects': related_objects}

    with open(os.path.join(prev, file_hash), 'wb') as f:
        pickle.dump(data, f)

    return file_hash


def load_from_shapshot(model, file_hash):
    """
    Load data from models .pickle snapshot
    """
    path = os.path.join(
        DRAFT_TMP_DIR,
        model._meta.app_label,
        model._meta.model_name,
        file_hash
    )

    with open(path, 'rb') as f:
        raw_data = pickle.load(f)

    instance = raw_data.pop('instance')
    related_objects = raw_data.pop('related_objects')
    instance._prefetched_objects_cache = related_objects

    # if related_objects:
    #     for k, v in related_objects.items():
    #         setattr(instance, '{}__draft'.format(k), v)

    return instance
