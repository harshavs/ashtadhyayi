#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.pratyahara import वर्णाः

class TestAardhadhatuka(unittest.TestCase):
    def test_अच्(self):
        self.assertEqual(वर्णाः('अच्'), '')

    def test_अस्(self):
        self.assertEqual(वर्णाः('अस्'), 'भू')

    def test_ग्लै(self):
        self.assertEqual(वर्णाः('ग्लै'), 'ग्ला')

if __name__ == '__main__':
    unittest.main()