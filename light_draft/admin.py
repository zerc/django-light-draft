# coding: utf-8
from __future__ import unicode_literals
from functools import update_wrapper

from django.core.exceptions import ImproperlyConfigured
from django.contrib import admin
from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied

from .utils import save_model_snapshot


class DraftAdmin(admin.ModelAdmin):
    """
    Mixin with draft view support
    """
    def get_urls(self):
        from django.conf.urls import url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        if not hasattr(self.model, 'get_absolute_url'):
            raise ImproperlyConfigured(
                "The model %s should have `.get_absolute_url` method "
                "to make possible to use the light-draft feature." % self.model
            )

        info = self.model._meta.app_label, self.model._meta.model_name

        return [
            url(
                r'^(.+)/preview/$',
                wrap(self.preview_view),
                name='%s_%s_preview' % info
            ),
        ] + super(DraftAdmin, self).get_urls()

    def preview_view(self, request, *args, **kwargs):
        model = self.model
        opts = model._meta

        if not self.has_add_permission(request):
            raise PermissionDenied

        ModelForm = self.get_form(request)
        obj = self.get_object(request, *args, **kwargs)

        if request.method != 'POST':
            raise Http404

        # Work with related formsets (collection instances)
        prefixes = {}
        items = {}
        for formset, inline in self.get_formsets_with_inlines(request, obj):
            prefix = formset.get_default_prefix()
            prefixes[prefix] = prefixes.get(prefix, 0) + 1
            if prefixes[prefix] != 1 or not prefix:
                prefix = "%s-%s" % (prefix, prefixes[prefix])

            formset = formset(request.POST, request.FILES,
                              instance=obj, prefix=prefix,
                              queryset=inline.get_queryset(request))

            items[formset.get_default_prefix()] = [
                f.save(commit=False) for f in formset
                if f.is_valid()]

        form = ModelForm(request.POST, request.FILES, instance=obj)
        form.just_preivew = True

        if form.is_valid():
            # Also proccess m2m fields
            opts = form.instance._meta

            # Model._meta.virtual_fields is removed in Django 2.0.x
            virtual_fields = getattr(opts, 'virtual_fields', [])

            for f in tuple(opts.many_to_many) + tuple(virtual_fields):
                if not hasattr(f, 'save_form_data'):
                    continue
                if form._meta.fields and f.name not in form._meta.fields:
                    continue
                if form._meta.exclude and f.name in form._meta.exclude:
                    continue
                if f.name in form.cleaned_data:
                    items[f.name] = form.cleaned_data[f.name]

            file_hash = save_model_snapshot(
                form.instance,
                related_objects=items
            )

            return HttpResponse(
                form.instance.get_absolute_url() + '?hash=' + file_hash)

        return HttpResponse(str(form.errors))

    class Media:
        js = ('admin/light.draft.js',)
