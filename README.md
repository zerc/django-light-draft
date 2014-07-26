django-light-draft
==================

Preview changes without saving the data in the db.

Install
-

Clone this repo inside your PYTHON PATH:

`git clone git@github.com:zerc/django-light-draft.git`

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

See `example/blog` app for more details.

NOTES
-

1. You models must define his own  `.get_absoulte_url ` method.
2. Preview for m2m relations now not support.
