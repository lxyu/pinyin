# -*- coding: utf-8 -*-

__all__ = ['get', 'get_pinyin', 'get_initial']

import os
import re

_punct_re = re.compile(ur'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.？]+')
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
        yield pinyin_dict.get(key, char), char


def get(s, delimiter=u''):
    """Return pinyin of string, the string must be unicode
    """
    assert(isinstance(s, unicode))
    words = []
    one_word = u""
    for word in _punct_re.split(s.lower()):
        for pinyin, char in _pinyin_generator(word):
            if pinyin != char:
                if one_word:
                    words.append(one_word)
                    one_word = u""
                words.append(pinyin)
            else:
                one_word += char

        if one_word:
            words.append(one_word)
            one_word = u""

    return unicode(delimiter.join(words))


# This function is only for backward compatibility, use `get` instead.
get_pinyin=get


def get_initial(s, delimiter=u' '):
    """Return the 1st char of pinyin of string, the string must be unicode
    """
    assert(isinstance(s, unicode))
    words = []
    for word in _punct_re.split(s.lower()):
        for pinyin, char in _pinyin_generator(word):
            words.append(pinyin[0])
    return unicode(delimiter.join(words))
