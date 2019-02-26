#!/usr/bin/env python
from setuptools import setup

setup(
    name='django-templates-email',
    version='1.0.0',
    description='',
    long_description='',
    author='Nicholas Wolff',
    author_email='nwolff@gmail.com',
    url='https://github.com/skioo/django-templates-email',
    packages=[
        'templates_email',
    ],
    install_requires=[
        'Django>=2.0,<2.2',
        'structlog',
        'typing',
        'django-render-block',
        'premailer',
        'lxml',
    ],
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
