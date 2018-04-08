.PHONY: clean-pyc clean-build clean

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "release - package and upload a release"
	@echo "test - run tests for current environment"
	@echo "test-all - run tests for all supported environments"
	@echo "install-dev - install dependencies for local development"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -not -path '*venv*' -exec rm -fr {} +
	find . -name '*.egg' -not -path '*venv*' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


release: clean
	python setup.py sdist upload

dist: clean
	python setup.py sdist
	ls -l dist

install: 
	python setup.py install

run: 
	python example/manage.py runserver 0.0.0.0:8000

test: clean
	cd example && python manage.py test

test-all: clean
	tox

install-dev: clean
	python setup.py develop
	pip install pip --upgrade
	pip install -r requirements.txt
