.. image:: https://raw.githubusercontent.com/zerc/django-light-draft/master/example/blog/static/images/DLD.png
   :alt: Django Light Draft

.. image:: https://travis-ci.org/zerc/django-light-draft.svg?branch=master
  :target: https://travis-ci.org/zerc/django-light-draft
.. image:: https://codecov.io/gh/zerc/django-light-draft/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/zerc/django-light-draft
  
Preview model changes without saving them into the database.  `Watch a demo <https://youtu.be/3pszDTUIfmg>`_ on YouTube.

Requirements:

* Django >= 1.8.x
* Python >= 2.7.x

Quickstart
----------

Instal the package via ``pip``:

.. code:: shell

    pip install django-light-draft

Add next lines to the ``settings.py`` of your project:

.. code:: python

    INSTALLED_APPS = (
        ...,
        'light_draft',
    )

    # Default settings. If you are happy with them - you can omit them.
    DRAFT_SETTINGS = {
        'cache_name': 'default',  # or any other cache you may have
        'ttl': 60*5,
    }


To make it work, you need to have at least ``default`` cache defined. If you are not familiar with this term check out `documentation <https://docs.djangoproject.com/en/2.0/topics/cache/>`_. In simpliest case you can enable in memory like this:

.. code:: python

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'just-an-example',
        }
    }


Then, in order to enable the feature for a particular model you need to make sure:

1. The admin model has been inherited from ``light_draft.admin.DraftAdmin``:

.. code:: python

    from light_draft.admin import DraftAdmin

    class MyModelAdmin(DraftAdmin):
        ...

2. The detail view of your model has been inherited from ``light_draft.views.BaseDraftView``:

.. code:: python

    from light_draft.views import BaseDraftView

    class MyModelDetailView(BaseDraftView):
        ...

3. The model has ``.get_absolute_url()`` method defined.

See ``example/blog`` app for more details.

Contributing
------------

See `CONTRIBUTING.md <CONTRIBUTING.md>`_ file for information how you can contribute to the project. Cheers!


Licence & Authors
-----------------

The MIT License (MIT)

Copyright (c) 2014 Vladimir Savin.
