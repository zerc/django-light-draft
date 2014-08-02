django-light-draft
==================

Preview changes without saving data into a db.

Install
-------

Usual way:

::

    pip install django-light-draft


Edit your settings.py:

.. code:: python

    INSTALLED_APPS = (
        ...

        'light_draft',

    )


Then you just need to inherit admin and detail views like this:

admin.py:

.. code:: python

    from light_draft.admin import DraftAdmin

    class MyModelAdmin(DraftAdmin):
        ...

views.py

.. code:: python

    from light_draft.views import BaseDraftView

    class MyModelDetailView(BaseDraftView):
        ...

To access many-to-one relation (inline forms in your admin change view) use  **model.<related_name>__draft**. 

Example:

.. code:: python

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


In preview mode your Page instance will have  **.blocks__draft** attribute to access the related models.

Example of using it in Django templates:

::

    {% for text_block in page.blocks__draft|default:page.blocks.all %}
        ...
    {% endfor %}

See **example/blog** app for more details.

NOTES
-----

1. Your models must define their own  **.get_absoulte_url** method.
2. Preview for m2m relations not supported yet.
