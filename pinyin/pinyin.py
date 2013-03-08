# -*- coding: utf-8 -*-

__all__ = ['get', 'get_pinyin', 'get_initial']

import os

# init pinyin dict
pinyin_dict = {}
dat = os.path.join(os.path.dirname(__file__), "Mandarin.dat")
with open(dat) as f:
    for line in f:
        k, v = line.strip().split('\t')
        pinyin_dict[k] = v.lower().split(" ")[0][:-1]


def _pinyin_generator(chars):
    """
    Generate pinyin for chars, if char is not chinese character,
    itself will be returned.
    Chars must be unicode list.
    """
    for char in chars:
        key = "%X" % ord(char)
        yield pinyin_dict.get(key, char)


def get(s, delimiter=''):
    """Return pinyin of string, the string must be unicode
    """
    assert(isinstance(s, unicode))
    return delimiter.join(_pinyin_generator(s))


# This function is only for backward compatibility, use `get` instead.
get_pinyin=get


def get_initial(s, delimiter=' '):
    """Return the 1st char of pinyin of string, the string must be unicode
    """
    assert(isinstance(s, unicode))
    return delimiter.join([p[0] for p in _pinyin_generator(s)])
