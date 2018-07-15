# coding: utf-8
from __future__ import unicode_literals
import os

from django.conf import settings

_default_draft_tmp_dir = os.path.join(settings.BASE_DIR, 'tmp')

# Deprecated. Use `DRAFT_SETTINGS` instead.
# Currently used only as a fallback. From now on, all writes go to the cache specified.
DRAFT_TMP_DIR = getattr(settings, 'DRAFT_TMP_DIR', _default_draft_tmp_dir)

DRAFT_SETTINGS = {
    'cache_name': 'default',
    'ttl': 60*5,
}
DRAFT_SETTINGS.update(getattr(settings, 'DRAFT_SETTINGS', {}))
