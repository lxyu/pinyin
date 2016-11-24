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
        'simplified': {}
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
        dictionaries['traditional'][traditional] = meaning
        dictionaries['simplified'][simplified] = meaning
        _add_to_tree(trees['traditional'], traditional, meaning)
        _add_to_tree(trees['simplified'], simplified, meaning)


def translate_word(word, dictionary=['simplified']):
    '''
    Return the set of translations for a single character or word, if
    available.
    '''
    if not dictionaries:
        init()
    for d in dictionary:
        if word in dictionaries[d]:
            return dictionaries[d][word]
    return None


def _words_at_the_beginning(word, tree, prefix=""):
    '''
    We return all portions of the tree corresponding to the beginning
    of `word`. This is used recursively, so we pass the prefix so we
    can return meaningful words+translations.
    '''
    l = []
    if "" in tree:
        l.append([prefix, tree[""]])
    if len(word) > 0 and word[0] in tree:
        l.extend(_words_at_the_beginning(
            word[1:],
            tree[word[0]],
            prefix=prefix+word[0]
        ))
    return l


def all_phrase_translations(phrase):
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
                    word[x+1:],
                    trees['simplified'][word[x]],
                    prefix=word[x]):
                yield translation
