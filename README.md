django-templates-email
======================

[![Build Status](https://travis-ci.org/skioo/django-templates-email.svg?branch=master)](https://travis-ci.org/skioo/django-templates-email)
[![PyPI version](https://badge.fury.io/py/django-templates-email.svg)](https://badge.fury.io/py/django-templates-email)
[![Requirements Status](https://requires.io/github/skioo/django-templates-email/requirements.svg?branch=master)](https://requires.io/github/skioo/django-templates-email/requirements/?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Generates the content needed to send a transactional email, based on a template:

The template should contains two blocks: "subject" and "html". The "html" block should contain a full html document,
with internal CSS styles in the <head> tag. When the template gets merged the CSS styles are automatically inlined.

A plaintext version of the html is automatically generated from the html (some email readers choose to display the plaintext).


Requirements
------------

* Python: 3.6 and over
* Django: 2.0 and over


Possible enhancement
--------------------
- Right now css inlining is applied each time an email is merged (and this takes time).
It would be better to 'pre-inline' once the basic html structure, and do the repetitive merges on that pre-inlined base.

One approach for implementation would be a custom 'css inlining' template loader.
Another would be a custom template tag that inlines during the compilation phase: https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#a-quick-overview


References
----------
- https://anymail.readthedocs.io/en/stable/tips/django_templates/ for premailer.
- https://github.com/vintasoftware/django-templated-email/ for the subject and html block idea.


To work on this code
--------------------

    pip install -e .

To run tests:

    tox

To release a version to pypi:
- Edit \_\_version\_\_ in \_\_init\_\_.py
- Push and wait for the build to succeed
- Create a release in github, travis will build and deploy the new version to pypi: https://pypi.python.org/pypi/django-templates-email

