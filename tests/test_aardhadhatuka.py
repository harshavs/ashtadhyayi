#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.aardhadhatuka import आर्धधातुकस्येड्_वलादेः_७_२_३५, धात्वादेश

class TestAardhadhatuka(unittest.TestCase):
    def test_पठ्_स्य(self):
        self.assertEqual(आर्धधातुकस्येड्_वलादेः_७_२_३५('पठ्', 'स्य'), 'पठिस्य')

    def test_अस्(self):
        self.assertEqual(धात्वादेश('अस्','सिप्'), 'भू')

    def test_ग्लै(self):
        self.assertEqual(धात्वादेश('ग्लै','सिप्'), 'ग्ला')

if __name__ == '__main__':
    unittest.main()


