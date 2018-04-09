# Contributing

1. Fork the `django-light-draft` repo on GitHub.
2. Clone your fork locally:

```shell
    git clone git@github.com:your_name_here/django-light-draft.git
```

3. Install and activate a virtual environment e.g. via `virtualenv`:

```shell
    cd django-light-draft/
    virtualenv venv
    source venv/bin/activate
```

4. Install the package for local development and all other dependencies (required to make the `example` work and run tests):

```shell
    make install-dev
```
    
5. Create a branch for local development:

```shell
    git checkout -b name-of-your-bugfix-or-feature
```

6. Hack the things!

7. When you're done making changes, check that your changes pass the tests, including testing other Python versions with [tox](https://tox.readthedocs.io/en/latest/):

```shell
    make test-all
```

To make all `tox` tests pass you need to make sure that you have all python versions listed in `tox.ini` installed in your system.
If, for some reason, you are not able to get them all, at least make sure that the tests pass for your current environment:

```shell
    make test
```

8. Commit your changes:

```shell
    git add .
    git commit -m "Detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature
```

9. Submit a pull request through the GitHub website.
