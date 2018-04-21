#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup


setup(
    name='starstr',
    version='1.0',
    author='Boyan Zhou',
    author_email='boyanzhou1992@gmail.com',
    packages=['starstr'],
    package_data={'starstr': []},
    scripts=['bin/starstr'],
    url='https://github.com/BoyanZhou/starstr',
    license='LICENSE.txt',
    description='Extract descent clusters from Y-STR data',
    long_description=open('README.md').read()
)
