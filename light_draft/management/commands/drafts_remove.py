# coding: utf-8
from __future__ import unicode_literals
import os
import glob
import shutil

from django.core.management.base import BaseCommand, CommandError

from light_draft.settings import DRAFT_TMP_DIR


class Command(BaseCommand):
    help = 'Remove all drafts from `{}` directory'.format(DRAFT_TMP_DIR)

    def handle(self, *args, **kwargs):
        if DRAFT_TMP_DIR in ('/', '/home/'):
            raise CommandError('suspect path .. >_>')

        self.stdout.write('>> REMOVING ALL DATA FROM {}'.format(DRAFT_TMP_DIR))

        for d in glob.glob(os.path.join(DRAFT_TMP_DIR, '*')):
            shutil.rmtree(d, False)

        self.stdout.write('>> DONE')
