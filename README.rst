django-light-draft
==================

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

1. Fork the ``django-light-draft`` repo on GitHub.
2. Clone your fork locally:

.. code:: shell

    git clone git@github.com:your_name_here/django-light-draft.git

3. Install and activate a virtual environment e.g. via ``virtualenv``:

.. code:: shell

    cd django-light-draft/
    virtualenv venv
    source venv/bin/activate

4. Install the package for local development and all other dependencies (required to make the ``example`` work and run tests):

.. code:: shell

    make install-dev
    
5. Create a branch for local development:

.. code:: shell

    git checkout -b name-of-your-bugfix-or-feature

6. Hack things!

7. When you're done making changes, check that your changes pass the tests, including testing other Python versions with ``tox``:

.. code:: shell

    make test-all

To make all ``tox`` tests pass you need to make sure that you have all python versions listed in ``tox.ini`` installed in your system.
If, for some reason, you are not able to get them all, at least make sure that the tests pass for your current environment:

.. code:: shell
    
    make test

8. Commit your changes:

.. code:: shell

    git add .
    git commit -m "Detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature

9. Submit a pull request through the GitHub website.


Licence & Authors
-----------------

The MIT License (MIT)

Copyright (c) 2014 Vladimir Savin.
