# -*- coding: utf-8 -*-

import unittest

import pinyin.cedict


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_pronounce_word(self):
        self.assertEqual(
            pinyin.cedict.pronounce_word("还是"),
            "hai2 shi5"
        )

    def test_translate_word(self):
        self.assertEqual(
            list(pinyin.cedict.translate_word("你好")),
            ['Hello!', 'Hi!', 'How are you?']
        )
        self.assertEqual(
            list(pinyin.cedict.translate_word("你")),
            ['you (informal, as opposed to courteous 您[nin2])']
        )

    def test_all_phrase_translations(self):
        self.assertEqual(
            list(pinyin.cedict.all_phrase_translations("你好")),
            [['你', ['you (informal, as opposed to courteous 您[nin2])']],
             ['你好', ['Hello!', 'Hi!', 'How are you?']],
             ['好', [
                 'to be fond of', 'to have a tendency to',
                 'to be prone to']]]
        )
        self.assertEqual(
            list(pinyin.cedict.all_phrase_translations("小兔子乖乖")),
            [['小', ['small', 'tiny', 'few', 'young']],
             ['兔', ['rabbit']],
             ['兔子', ['hare', 'rabbit', 'CL:隻|只[zhi1]']],
             ['子', ['(noun suffix)']],
             ['乖', [
                 '(of a child) obedient, well-behaved', 'clever',
                 'shrewd', 'alert', 'perverse', 'contrary to reason',
                 'irregular', 'abnormal']],
             ['乖', [
                 '(of a child) obedient, well-behaved', 'clever',
                 'shrewd', 'alert', 'perverse', 'contrary to reason',
                 'irregular', 'abnormal']]]
        )
        self.assertEqual(
            list(pinyin.cedict.all_phrase_translations(
                "刻是梦还是真", include_pinyin=True)),
            [['刻', 'kè', ['quarter (hour)', 'moment', 'to carve', 'to engrave', 'to cut',
                          'oppressive', 'classifier for short time intervals']],
             ['是', 'shì', ['variant of 是[shi4]', '(used in given names)']],
             ['梦', 'mèng', ['dream', 'CL:場|场[chang2],個|个[ge4]']],
             ['还', 'huán', ['to pay back', 'to return']],
             ['还是', 'hái shi', ['or', 'still', 'nevertheless', 'had better']],
             ['是', 'shì', ['variant of 是[shi4]', '(used in given names)']],
             ['真', 'zhēn', ['really', 'truly', 'indeed', 'real', 'true', 'genuine']]]
        )


if __name__ == '__main__':
    unittest.main()
