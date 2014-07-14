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

    all_fields = [instance._meta.get_field_by_name(f)[0] for f
                  in instance._meta.get_all_field_names()]

    # saving FK and M2M fields makes not sense - exclude it
    exclude = [f.name for f in all_fields if isinstance(f, RelatedField)]
    _dict = model_to_dict(instance, exclude=exclude)

    with open(os.path.join(prev, file_hash), 'wb') as f:
        pickle.dump(_dict, f)

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

    with open(path, 'rb') as w:
        data_dict = pickle.load(w)
        return model(**data_dict)
