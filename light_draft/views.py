# coding: utf-8
from __future__ import unicode_literals

from django.http import Http404
from django.views.generic.detail import DetailView

from .utils import load_from_shapshot
from .exceptions import DraftError


class BaseDraftView(DetailView):
    """
    View for loading data from model `snapshot`
    """
    def get_template_names(self):
        names = super(BaseDraftView, self).get_template_names()
        preview = names[0].replace('.html', '_preview.html')
        names.insert(0, preview)
        return names

    def get_object(self, *args, **kwargs):
        if getattr(self, '__object', None):
            return self.__object

        if 'hash' in self.request.GET:
            try:
                self.__object = load_from_shapshot(
                    self.model, self.request.GET.get('hash'))
            except DraftError:
                raise Http404('Snapshot does not exist')
            return self.__object

        return super(BaseDraftView, self).get_object(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(BaseDraftView, self).get_context_data(*args, **kwargs)
        context['is_draft_preview'] = True
        return context
