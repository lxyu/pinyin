#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

# init pinyin dict
PINYIN_DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'Mandarin.dat')
pinyin_dict = {}
with open(PINYIN_DATA) as f:
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


def get_pinyin(string):
    """
    Return pinyin of string, the input string must be unicode
    """
    if type(string) is not unicode:
        raise AttributeError('Input string is not unicode: %s' % string)

    generator = pinyin_generator(string)
    return ''.join(generator)


def get_pinyin_first_char(string):
    """
    Return the 1st char of pinyin of string, the input string must be unicode
    """
    if type(string) is not unicode:
        raise AttributeError('Input string is not unicode: %s' % string)

    generator = pinyin_generator(string)
    return ''.join([p[0] for p in generator])
