django-light-draft
==================

Preview changes without saving the data in the db.

Install
-
Usual way:

`pip install django-light-draft`


Edit you settings.py:
```
INSTALLED_APPS = (
    ...

    'light_draft',
)
```

Then you need just inherit admin and detail views like this:

admin.py:
```
from light_draft.admin import DraftAdmin

class MyModelAdmin(DraftAdmin):
    ...
```

views.py
```
from light_draft.views import BaseDraftView

class MyModelDetailView(BaseDraftView):
    ...
```

For access to many-to-one relation (inline forms in you admin change view) use  `model.<related_name>__draft`. Example:

```
# models.py
class Page(models.Model):
    title = models.CharField(max_length="225")


class PageBlock(models.Model):
    page = models.ForeignKey(Page, related_name="blocks")
    body = models.TextField()


# admin.py
class PageBlockAdmin(TabularInline):
    model = PageBlock


class PageAdmin(admin.ModelAdmin):
    inlines = [PageBlockAdmin]


admin.register(Page, PageAdmin)

```

In preview mode yours Page instance will have  ` .blocks__draft` attr to access the related models.

Example of using it in Django templates:

```
{% for text_block in page.blocks__draft|default:page.blocks.all %}
    ...
{% endfor %}
```

See `example/blog` app for more details.

NOTES
-

1. You models must define his own  `.get_absoulte_url ` method
2. Preview for m2m relations now not support.
