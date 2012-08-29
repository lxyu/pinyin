Pinyin Translator
=================

Translate chinese chars to pinyin based on Mandarin.dat

Usage
-----

Input unicode string

::

    >>> import pinyin
    >>> pinyin.get_pinyin(u'你好')
    'nihao'
    >>> pinyin.get_initial(u'你好')
    'n h'
