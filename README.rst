django-light-draft
==================

.. image:: https://travis-ci.org/zerc/django-light-draft.svg?branch=master
    :target: https://travis-ci.org/zerc/django-light-draft
.. image:: https://codecov.io/gh/zerc/django-light-draft/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/zerc/django-light-draft
  

Preview model changes without saving the data into the database.

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


See **example/blog** app for more details.


NOTES
-----

1. Your models have to define their own  **.get_absoulte_url** method.
