#!/usr/bin/env python

import codecs
import os.path
import re
import sys

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


install_requires = [
    'Click',
    'dhcp-leases',
]


setup_options = dict(
    name='btklog',
    version='1.0.2',
    packages=find_packages(),
    include_package_data=True,
    description='Generates IP logs compatible with Turkey 5651 law from dhcpd.leases format.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Ogun Acik',
    url='https://github.com/acikogun/btklog',
    author_email='acikogun@gmail.com',
    install_requires=install_requires,
    entry_points='''
        [console_scripts]
        btklog=btklog.btklog:btklog
    ''',
    license="Apache License 2.0",
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: Turkish',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

setup(**setup_options)
