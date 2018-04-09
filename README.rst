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

Add it to the ``settings.py`` of your project:

.. code:: python

    INSTALLED_APPS = (
        ...,
        'light_draft',
    )

To enable the feature for a particular model you need to make sure:

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
