#!/usr/bin/env python
from setuptools import setup

import templates_email

setup(
    name='django-templates-email',
    version=templates_email.__version__,
    description='',
    long_description='',
    author='Nicholas Wolff',
    author_email='nwolff@gmail.com',
    url=templates_email.__URL__,
    packages=[
        'templates_email',
    ],
    install_requires=[
        'Django>=1.7',
        'structlog',
        'typing',
        'django-render-block',
        'premailer',
        'lxml',
    ],
    license=templates_email.__licence__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ],
)
