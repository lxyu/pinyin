Pinyin
======

.. image:: https://badge.fury.io/py/pinyin.png
    :target: http://badge.fury.io/py/pinyin

.. image:: https://travis-ci.org/lxyu/pinyin.png?branch=master
    :target: https://travis-ci.org/lxyu/pinyin

.. image:: https://pypip.in/d/pinyin/badge.png
    :target: https://crate.io/packages/pinyin/

Translate chinese chars to pinyin based on Mandarin.dat

Install
-------

.. code:: bash

    $ pip install pinyin

Usage
-----

.. code:: python

    >>> import pinyin
    >>> pinyin.get(u'你好')
    'nihao'
    >>> pinyin.get_initial(u'你好')
    'n h'
