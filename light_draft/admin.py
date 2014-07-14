# coding: utf-8
from __future__ import unicode_literals
from functools import update_wrapper

from django.contrib import admin
from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied

from .utils import save_model_snapshot


class DraftAdmin(admin.ModelAdmin):
    """
    Mixin with draft view support
    """
    def get_urls(self):
        from django.conf.urls import patterns, url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.model_name

        if not hasattr(self.model, 'get_draft_url'):
            super(DraftAdmin, self).get_urls()

        return patterns('',
                        url(r'^(.+)/preview/$',
                            wrap(self.preview_view),
                            name='%s_%s_preview' % info),
                        ) + super(DraftAdmin, self).get_urls()

    def preview_view(self, request, *args, **kwargs):
        model = self.model
        opts = model._meta

        if not self.has_add_permission(request):
            raise PermissionDenied

        ModelForm = self.get_form(request)
        if request.method == 'POST':
            form = ModelForm(request.POST, request.FILES)
            form.just_preivew = True

            if form.is_valid():
                file_hash = save_model_snapshot(form.instance)
                return HttpResponse(
                    form.instance.get_draft_url() + '?hash=' + file_hash)

        raise Http404
