# -*- coding: utf-8 -*-

import unittest

import pinyin


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get(self):
        self.assertEqual(pinyin.get(u'你好'), 'nihao')
        self.assertEqual(pinyin.get(u'你好吗?'), 'nihaoma?')
        self.assertEqual(pinyin.get(u'你好吗？'), u'nihaoma\uff1f')

        self.assertEqual(pinyin.get('你好'.decode('utf-8')), u'nihao')

    def test_get_with_delimiter(self):
        self.assertEqual(pinyin.get(u'你好', " "), 'ni hao')
        self.assertEqual(pinyin.get(u'你好吗?', " "), 'ni hao ma ?')
        self.assertEqual(pinyin.get(u'你好吗？', " "), u'ni hao ma \uff1f')

    def test_get_initial_with_delimiter(self):
        self.assertEqual(pinyin.get_initial(u'你好', "-"), 'n-h')
        self.assertEqual(pinyin.get_initial(u'你好吗?', "-"), 'n-h-m-?')
        self.assertEqual(pinyin.get_initial(u'你好吗？', "-"), u'n-h-m-？')

    def test_get_initial(self):
        self.assertEqual(
            pinyin.get_initial(u'你好'), 'n h')
        self.assertEqual(
            pinyin.get_initial(u'你好吗?'), 'n h m ?')
        self.assertEqual(
            pinyin.get_initial(u'你好吗？'), u'n h m ？')

        self.assertEqual(
            pinyin.get_initial('你好'.decode('utf-8')), 'n h')

    def test_mixed_chinese_english_input(self):
        self.assertEqual(pinyin.get(u'hi你好'), 'hinihao')

    def test_unicode_assertion(self):
        self.failUnlessRaises(AssertionError, pinyin.get, '你好')


if __name__ == '__main__':
    unittest.main()
