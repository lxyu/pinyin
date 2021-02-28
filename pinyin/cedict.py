#!/usr/local/bin/python
# -*- coding: utf-8 -*-

'''
A utility to translate Mandarin to English. The data file is from
the CEDICT project. We keep it compressed for size and speed.

Using this has substantial (1-2 second) init time for reading the
dictionary. This is spent the first time this module is used (it
is free to import).

Note that this is a prototype. It is specific to Python 3. To bring
this code to the quality level of the rest of the library, it would
need to be backported to Python 2.

In addition, it'd be nice if `all_phrase_translations` handled both
traditional and simplified elegantly.
'''

import gzip
import os.path
import re
import string
import collections
from pinyin import numerical_to_diacritical


def Tree():
    return collections.defaultdict(Tree)


dictionaries = None  # Used for single word lookup
trees = None  # Used for parsing.


def _add_to_tree(tree, word, meaning):
    '''
    We build word search trees, where we walk down
    the letters of a word. For example:
      你 Good
      你好 Hello
    Would build the tree
         你
        /  \
      You   好
             \
           Hello
    '''
    if len(word) == 0:
        tree[''] = meaning
    else:
        _add_to_tree(tree[word[0]], word[1:], meaning)


def init():
    '''
    Load in the Chinese-English dictionary. This takes 1-2 seconds. It
    is done when the other functions are used, but this is public since
    preloading sometimes makes sense.
    '''
    global dictionaries, trees

    dictionaries = {
        'traditional': {},
        'simplified': {},
        'pinyin': {}
    }

    trees = {
        'traditional': Tree(),
        'simplified': Tree()
    }

    lines = gzip.open(
        os.path.join(os.path.dirname(__file__), "cedict.txt.gz"),
        mode='rt',
        encoding='utf-8'
    )
    exp = re.compile("^([^ ]+) ([^ ]+) \[(.*)\] /(.+)/")
    parsed_lines = (exp.match(line).groups()
                    for line in lines
                    if line[0] != '#')

    for traditional, simplified, pinyin, meaning in parsed_lines:
        meaning = meaning.split('/')
        meaning = (pinyin, meaning)
        dictionaries['traditional'][traditional] = meaning
        dictionaries['simplified'][simplified] = meaning
        dictionaries['pinyin'][simplified] = pinyin
        _add_to_tree(trees['traditional'], traditional, meaning)
        _add_to_tree(trees['simplified'], simplified, meaning)


def pronounce_word(word):
    return dictionaries['pinyin'].get(word)


def translate_word(word, dictionary=['simplified']):
    '''
    Return the set of translations for a single character or word, if
    available.
    '''
    if not dictionaries:
        init()
    for d in dictionary:
        if word in dictionaries[d]:
            return dictionaries[d][word][1]
    return None


def _words_at_the_beginning(word, tree, prefix="", include_pinyin=False):
    '''
    We return all portions of the tree corresponding to the beginning
    of `word`. This is used recursively, so we pass the prefix so we
    can return meaningful words+translations.
    '''
    l = []
    if "" in tree:
        pinyin, meaning = tree[""]
        l.append([prefix, pinyin, meaning])
    if len(word) > 0 and word[0] in tree:
        l.extend(
            _words_at_the_beginning(
                word[1:],
                tree[word[0]],
                prefix=prefix + word[0],
                include_pinyin=include_pinyin,
            )
        )
    return l


def all_phrase_translations(phrase, dictionary='simplified', include_pinyin=False, format='diacritical'):
    '''
    Return the set of translations for all possible words in a full
    phrase. Chinese is sometimes ambiguous. We do not attempt to
    disambiguate, or handle unknown letters especially well. Full
    parsing is left to upstream logic.
    '''
    if not trees:
        init()
    phrase = phrase.split(string.whitespace)
    for word in phrase:
        for x in range(len(word)):
            for translation in _words_at_the_beginning(
                word[x + 1:],
                trees[dictionary][word[x]],
                prefix=word[x],
                include_pinyin=include_pinyin,
            ):
                characters, pinyin, meaning = translation
                if include_pinyin:
                    if format == 'diacritical':
                        pinyin = numerical_to_diacritical(pinyin)
                    yield [characters, pinyin, meaning]
                else:
                    yield [characters, meaning]
