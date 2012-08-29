#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['get_pinyin', 'get_initial']

import os

# init pinyin dict
dat = os.path.join(os.path.dirname(__file__), "Mandarin.dat")
pinyin_dict = {}
with open(dat) as f:
    for line in f:
        k, v = line.strip().split('\t')
        pinyin_dict[k] = v.lower().split(" ")[0][:-1]


def pinyin_generator(chars):
    """
    Generate pinyin for chars, if char is not chinese character,
    itself will be returned.
    Chars must be unicode list.
    """
    for char in chars:
        key = "%X" % ord(char)
        yield pinyin_dict.get(key, char)


def get_pinyin(s):
    """
    Return pinyin of string, the input string must be unicode
    """
    assert(type(s) is unicode)

    generator = pinyin_generator(s)
    return ''.join(generator)


def get_initial(s):
    """
    Return the 1st char of pinyin of string, the input string must be unicode
    """
    assert(type(s) is unicode)

    generator = pinyin_generator(s)
    return ' '.join([p[0] for p in generator])
