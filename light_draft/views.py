# coding: utf-8
from __future__ import unicode_literals

from django.http import Http404
from django.views.generic.detail import DetailView

from .utils import load_from_shapshot


class BaseDraftView(DetailView):
    """
    View for loading data from model `snapshot`
    """
    template_name_suffix = '_preview'

    def get_object(self, *args, **kwargs):
        if getattr(self, '__object', None):
            return self.__object

        if not 'hash' in self.request.GET:
            raise Http404

        self.__object = load_from_shapshot(
            self.model, self.request.GET.get('hash'))

        return self.__object
