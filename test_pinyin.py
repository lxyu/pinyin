# -*- coding: utf-8 -*-

import unittest

import pinyin


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_unicode_pinyin(self):
        self.assertEqual(pinyin.get_pinyin(u'你好'), u'nihao')
        self.assertEqual(pinyin.get_pinyin(u'你好吗?'), u'nihaoma?')
        self.assertEqual(pinyin.get_pinyin(u'你好吗？'), u'nihaoma\uff1f')

        self.assertEqual(pinyin.get_pinyin('你好'.decode('utf-8')), u'nihao')

    def test_unicode_pinyin_first_char(self):
        self.assertEqual(
            pinyin.get_pinyin_first_char(u'你好'), u'nh')
        self.assertEqual(
            pinyin.get_pinyin_first_char(u'你好吗?'), u'nhm?')
        self.assertEqual(
            pinyin.get_pinyin_first_char(u'你好吗？'), u'nhm\uff1f')

        self.assertEqual(
            pinyin.get_pinyin_first_char('你好'.decode('utf-8')), u'nh')

    def test_mixed_chinese_english_input(self):
        self.assertEqual(pinyin.get_pinyin(u'hi你好'), u'hinihao')

    def test_not_unicode_exception(self):
        self.failUnlessRaises(AttributeError, pinyin.get_pinyin, '你好')


if __name__ == '__main__':
    unittest.main()
