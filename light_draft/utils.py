# coding: utf-8
from __future__ import unicode_literals
import os
import cPickle as pickle
from uuid import uuid4

from django.conf import settings
from django.db.models.fields.related import RelatedField
from django.forms.models import model_to_dict


TMP_DIR = getattr(settings, 'TMP_DIR', 'tmp')


def save_model_snapshot(instance):
    """
    Serialize instance into .pickle cache file
    """
    parts = (
        TMP_DIR,
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

    with open(os.path.join(prev, file_hash), 'wb') as f:
        pickle.dump(instance, f)

    return file_hash


def load_from_shapshot(model, file_hash):
    """
    Load data from models .pickle snapshot
    """
    path = os.path.join(
        TMP_DIR,
        model._meta.app_label,
        model._meta.model_name,
        file_hash
    )

    with open(path, 'rb') as f:
        return pickle.load(f)
