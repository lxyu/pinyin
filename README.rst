Pinyin
======

.. image:: http://img.shields.io/pypi/v/pinyin.svg?style=flat
   :target: https://pypi.python.org/pypi/pinyin

.. image:: http://img.shields.io/travis/lxyu/pinyin/master.svg?style=flat
   :target: https://travis-ci.org/lxyu/pinyin


Translate chinese chars to pinyin based on Mandarin.dat

Install
-------

.. code:: bash

    $ pip install pinyin

Usage
-----

.. code:: python

    >>> import pinyin
    >>> print pinyin.get('你 好')
    nǐ hǎo

    >>> print pinyin.get('你好', format="strip", delimiter=" ")
    ni hao

    >>> print pinyin.get('你好', format="numerical")
    ni3hao3

    >>> print pinyin.get_initial('你好')
    n h

.. note::

    `format` must be one of: numerical/diacritical/strip

Prototype Chinese->English
--------------------------

.. code:: python

    >>> import pinyin.cedict
    >>> pinyin.cedict.translate_word('你')
    ['you (informal, as opposed to courteous 您[nin2])']
    >>> pinyin.cedict.translate_word('你好')
    ['Hello!', 'Hi!', 'How are you?']
    >>> list(pinyin.cedict.all_phrase_translations('你好'))
    [['你', ['you (informal, as opposed to courteous 您[nin2])']], ['你好', ['Hello!', 'Hi!', 'How are you?']], ['好', ['to be fond of', 'to have a tendency to', 'to be prone to']]]

Note that this is a prototype, and only functions from Python 3.

License
-------

`pinyin` is free software, under an MIT-style license. See LICENSE for details.

The data file for translations is the CC-BY-SA 3.0.

The translations are from the CC-CE-DICT project (https://cc-cedict.org/wiki/), by Denisowski, Peterson, Brelsford, and others.
