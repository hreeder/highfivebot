#!/usr/bin/env python
# -*- coding: utf8 -*-
import os.path

from setuptools import setup

install_requires = [
    'logbook',
    'tornado',
    'possel-server',
]

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Topic :: Communications :: Chat :: Internet Relay Chat',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3 :: Only',
]

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme_file:
    long_description = readme_file.read()

setup(
    # Metadata
    name='highfivebot',
    version='0.1.0',
    author='Kit Barnes',
    author_email='kit@ninjalith.com',
    description='',
    long_description=long_description,
    url='https://bitbucket.org/KitB/possel/',
    license='BSD',
    keywords='irc quassel',
    classifiers=classifiers,
    zip_safe=False,

    # Non-metadata (mostly)
    packages=[],
    py_modules=['hfb'],
    install_requires=install_requires,
    extras_require={},
    scripts=['bin/hfb'],
    package_data={},
)
