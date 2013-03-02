Pinyin
======

.. image:: https://travis-ci.org/lxyu/pinyin.png?branch=master

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
