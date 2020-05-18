#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.sajna import हलोऽनन्तराः_संयोगः_१_१_७, अचोऽन्त्यादि_टि_१_१_६४


class TestSajna(unittest.TestCase):
    def test_हलोऽनन्तराः_संयोगः_१_१_७_अग्नि(self):
        self.assertEqual(हलोऽनन्तराः_संयोगः_१_१_७('अग्नि').group(), 'ग्न')

    def test_हलोऽनन्तराः_संयोगः_१_१_७_बुद्ध्या(self):
        self.assertEqual(हलोऽनन्तराः_संयोगः_१_१_७('बुद्ध्या').group(), 'द्ध्य')

    def test_हलोऽनन्तराः_संयोगः_१_१_७_पुत्त्र्या(self):
        self.assertEqual(हलोऽनन्तराः_संयोगः_१_१_७('पुत्त्र्या').group(), 'त्त्र्य')

    def test_हलोऽनन्तराः_संयोगः_१_१_७_कार्त्स्न्य(self):
        self.assertEqual(हलोऽनन्तराः_संयोगः_१_१_७('कार्त्स्न्य').group(), 'र्त्स्न्य')

    def test_अचोऽन्त्यादि_टि_१_१_६४(self):
        self.assertEqual(अचोऽन्त्यादि_टि_१_१_६४('आथाम्'), 'आम्')


if __name__ == '__main__':
    unittest.main()
