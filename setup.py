#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='pinyin',
    version='0.3.1',
    description='Translate chinese chars to pinyin based on Mandarin.dat',
    author='Lx Yu',
    author_email='github@lxyu.net',
    packages=['pinyin', ],
    package_data={'': ['LICENSE'], 'pinyin': ['Mandarin.dat'], },
    entry_points={"console_scripts": ["pinyin = pinyin.cmd:pinyin", ]},
    url='http://lxyu.github.io/pinyin/',
    license="BSD",
    long_description=open('README.rst').read(),
    classifiers=[
        "Topic :: Software Development",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ]
)
