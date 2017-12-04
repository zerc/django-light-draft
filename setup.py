# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='django-light-draft',
    version='0.4.0',
    author='Vladimir Savin',
    author_email='zero13cool@yandex.ru',

    description='Preview changes without saving the data into db.',
    long_description=open('README.rst').read(),
    url='https://github.com/zerc/django-light-draft',
    license='MIT',

    packages=find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'django>=1.8,<2.0',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',

        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
