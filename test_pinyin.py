# -*- coding: utf-8 -*-

import unittest

import pinyin
from pinyin._compat import u


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get(self):
        self.assertEqual(pinyin.get('你好'),
                         pinyin.get('你好', format="diacritical"))
        self.assertEqual(pinyin.get(u('你好'), format="strip"), u('nihao'))
        self.assertEqual(pinyin.get(u('你好'), format="numerical"), u('ni3hao3'))
        self.assertEqual(pinyin.get(u('你好'), format="diacritical"), u('nǐhǎo'))
        self.assertEqual(pinyin.get('你好吗?'), u('nǐhǎoma?'))
        self.assertEqual(pinyin.get('你好吗？'), u('nǐhǎoma？'))

        self.assertEqual(pinyin.get('你好'), u('nǐhǎo'))
        self.assertEqual(pinyin.get('叶'), u('yè'))

    def test_get_with_delimiter(self):
        self.assertEqual(pinyin.get('你好', " "), u('nǐ hǎo'))
        self.assertEqual(pinyin.get('你好吗?', " "), u('nǐ hǎo ma ?'))
        self.assertEqual(pinyin.get('你好吗？', " "), u('nǐ hǎo ma ？'))

    def test_get_initial_with_delimiter(self):
        self.assertEqual(pinyin.get_initial('你好', "-"), u('n-h'))
        self.assertEqual(pinyin.get_initial('你好吗?', "-"), u('n-h-m-?'))
        self.assertEqual(pinyin.get_initial('你好吗？', "-"), u('n-h-m-？'))

    def test_get_initial(self):
        self.assertEqual(pinyin.get_initial('你好'), u('n h'))
        self.assertEqual(pinyin.get_initial('你好吗?'), u('n h m ?'))
        self.assertEqual(pinyin.get_initial('你好吗？'), u('n h m ？'))

        self.assertEqual(pinyin.get_initial('你好'), 'n h')

    def test_mixed_chinese_english_input(self):
        self.assertEqual(pinyin.get('hi你好'), u('hinǐhǎo'))


if __name__ == '__main__':
    unittest.main()
