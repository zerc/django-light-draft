# coding: utf-8
from __future__ import unicode_literals
import os

from django.conf import settings

_default_draft_tmp_dir = os.path.join(settings.BASE_DIR, 'tmp')

DRAFT_TMP_DIR = getattr(settings, 'DRAFT_TMP_DIR', _default_draft_tmp_dir)
