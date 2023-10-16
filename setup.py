#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import open

from setuptools import setup

setup(
    name='pinyin-hitalent',
    version='0.4.1',
    description='Translate chinese chars to pinyin based on Mandarin.dat',
    author='Lx Yu + Piotr Mitros + Hao Guo',
    author_email='github@lxyu.net',
    packages=['pinyin', ],
    package_data={
        '': ['LICENSE'],
        'pinyin': ['Mandarin.dat', 'cedict.txt.gz'], },
    entry_points={"console_scripts": ["pinyin = pinyin.cmd:pinyin", ]},
    url='http://lxyu.github.io/pinyin/',
    license="BSD",
    long_description=open('README.rst', encoding='utf-8').read(),
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
