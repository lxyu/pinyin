Pinyin
======

.. image:: http://img.shields.io/pypi/v/pinyin.svg?style=flat
   :target: https://pypi.python.org/pypi/pinyin

.. image:: http://img.shields.io/travis/lxyu/pinyin/master.svg?style=flat
   :target: https://travis-ci.org/lxyu/pinyin

.. image:: http://img.shields.io/pypi/dm/pinyin.svg?style=flat
   :target: https://pypi.python.org/pypi/pinyin


Translate chinese chars to pinyin based on Mandarin.dat

Install
-------

.. code:: bash

    $ pip install pinyin

Usage
-----

.. code:: python

    >>> import pinyin
    >>> pinyin.get('你好')
    'nihao'
    >>> pinyin.get_initial('你好')
    'n h'
