# -*- coding: utf-8 -*-

import unittest

import pinyin


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get(self):
        self.assertEqual(pinyin.get(u'你好'), u'nihao')
        self.assertEqual(pinyin.get(u'你好吗?'), u'nihaoma?')
        self.assertEqual(pinyin.get(u'你好吗？'), u'nihaoma\uff1f')

        self.assertEqual(pinyin.get('你好'.decode('utf-8')), u'nihao')

    def test_get_initial(self):
        self.assertEqual(
            pinyin.get_initial(u'你好'), u'n h')
        self.assertEqual(
            pinyin.get_initial(u'你好吗?'), u'n h m ?')
        self.assertEqual(
            pinyin.get_initial(u'你好吗？'), u'n h m ？')

        self.assertEqual(
            pinyin.get_initial('你好'.decode('utf-8')), u'n h')

    def test_mixed_chinese_english_input(self):
        self.assertEqual(pinyin.get(u'hi你好'), u'hinihao')

    def test_unicode_assertion(self):
        self.failUnlessRaises(AssertionError, pinyin.get_pinyin, '你好')


if __name__ == '__main__':
    unittest.main()
