# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='advanced-data-structures',
    description='A collection of slightly more advanced data structures',
    version=0.1,
    author='Paul Sheirdan and Rick Tesmond',
    author_email='paul.sheridan@me.com and tesmonrd@gmail.com',
    license='MIT',
    py_modules=['bst'],
    package_dir={'': 'src'},
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
)
