#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-fixturemedia',
    version='0.1',
    description='Simple tool to manage media files for fixtures.',
    packages=['fixturemedia', 'fixturemedia.management', 'fixturemedia.management.commands'],
)
