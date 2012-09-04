#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='pinyin',
    version='0.1.2',
    description='Translate chinese chars to pinyin based on Mandarin.dat',
    author='Lx Yu',
    author_email='lixinfish@gmail.com',
    packages=['pinyin', ],
    package_data={'': ['LICENSE'], 'pinyin': ['Mandarin.dat'], },
    scripts=['bin/pinyin'],
    url='http://lxyu.github.com/pinyin/',
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
)
