#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.purvatraasiddham import आदेशप्रत्यययोः_८_३_५९


class TestPurvatraasiddham(unittest.TestCase):
    def test_आदेशप्रत्यययोः_८_३_५९_वाक्षु(self):
        self.assertEqual(आदेशप्रत्यययोः_८_३_५९('वाक्', 'सुप्'), 'षुप्')

    def test_आदेशप्रत्यययोः_८_३_५९_पठिष्यति(self):
        self.assertEqual(आदेशप्रत्यययोः_८_३_५९('इ', 'स्य'), 'ष्य')

    def test_आदेशप्रत्यययोः_८_३_५९_सिषेच(self):
        self.assertEqual(आदेशप्रत्यययोः_८_३_५९('सि', 'सेच'), 'षेच')


if __name__ == '__main__':
    unittest.main()
