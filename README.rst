Pinyin
======

.. image:: https://badge.fury.io/py/pinyin.png
   :target: http://badge.fury.io/py/pinyin

.. image:: https://travis-ci.org/lxyu/pinyin.png?branch=master
   :target: https://travis-ci.org/lxyu/pinyin

.. image:: https://pypip.in/d/pinyin/badge.png
   :target: https://crate.io/packages/pinyin/

.. image:: https://d2weczhvl823v0.cloudfront.net/lxyu/pinyin/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free


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
