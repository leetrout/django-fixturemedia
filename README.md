django-fixture-media
===================

[![Build Status](https://travis-ci.org/leetrout/django-fixturemedia.png?branch=master)](https://travis-ci.org/leetrout/django-fixturemedia)

_Renamed 11/21/2013_

Simple tool to manage media files for fixtures. Contributions welcome.

Put relative paths in your fixtures, put your media files in a media directory
in you fixtures directory.

Run `collectmedia` and your fixture media will be copied to MEDIA_ROOT.


YMMV
----

Only supports JSON and YAML fixtures.


Installation
------------

Using pip:

    pip install django-fixture-media

Add `'fixture_media'` to your installed apps.

Manual install:

Download the source code and run `python setup.py install` within the directory

Add `'fixture_media'` to your installed apps.


Usage
-----

1. Add relative paths to your fixtures for file / image fields.


        [
            {
                "pk": 1,
                "model": "myapp.mymodel",
                "fields": {
                    "name": "Awesome Sauce",
                    "image": "images/awesome-sauce.jpg"
                }
            }
        ]


2. Add a `media` directory in your fixtures directory. Add the matching
child directories to match the path in the fixture and place your media file
in the appropriate location.


        myapp/
            models.py
            fixtures/
                initial_data.json
                media/
                    images/
                        awesome-sauce.jpg


3. Run `django-admin.py collectmedia` or `manage.py collectmedia`


        ./manage.py collectmedia
        This will overwrite any existing files. Proceed? yes
        Copied images/awesome-sauce.jpg to /tmp/django_media/images/awesome-sauce.jpg


CONFIGURATION
-------------

* `FIXTURE_MEDIA_REQUIRE_PREFIX` (default: `False`)

  By default, the management command will try to copy everything that resembles
  a file path; if you have a lot of entries in your fixtures that looks like
  file paths but is not actually one, you can specify
  `FIXTURE_MEDIA_REQUIRE_PREFIX = True` in settings.py to make 
  `./manage.py collectmedia` copy only files that are prefixed with `media://`.

  Example:

        [
            {
                "pk": 1,
                "model": "myapp.mymodel",
                "fields": {
                    "name": "Awesome Sauce",
                    "image": "media://images/awesome-sauce.jpg"
                    "path": "this/is/ignored/awesome-sauce.jpg"
                }
            }
        ]

Thanks
------
lieryan
swiharta


TODO
----

+ Add tests.
+ Convert to better command modeled after the excellent staticfiles app.
