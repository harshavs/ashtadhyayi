#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.sajna import वृद्धिरादैच्_१_१_१, अदेङ्_गुणः_१_१_२, इको_गुणवृद्धी_१_१_३
from ashtadhyayi.sajna import हलोऽनन्तराः_संयोगः_१_१_७, अचोऽन्त्यादि_टि_१_१_६४, अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५
from ashtadhyayi.sajna import मिदचोऽन्त्यात्परः_१_१_४७


class TestSajna(unittest.TestCase):
    def test_वृद्धिरादैच्_१_१_१(self):
        self.assertEqual(वृद्धिरादैच्_१_१_१(), ['आ', 'ऐ', 'औ'])

    def test_अदेङ्_गुणः_१_१_२(self):
        self.assertEqual(अदेङ्_गुणः_१_१_२(), ['अ', 'ए', 'ओ'])

    def test_इको_गुणवृद्धी_१_१_३(self):
        self.assertEqual(इको_गुणवृद्धी_१_१_३('इ'), 'ए')

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

    def test_अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५_रामम्(self):
        self.assertEqual(अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५('रामम्'), 'अ')

    def test_अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५_पृच्छ्(self):
        self.assertEqual(अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५('पृच्छ्'), 'च्')

    def test_अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५_कृष्ण(self):
        self.assertEqual(अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५('कृष्ण'), 'ण्')

    def test_अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५_देवः(self):
        self.assertEqual(अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५('देवः'), 'अ')

    def test_मिदचोऽन्त्यात्परः_१_१_४७_वद्(self):
        self.assertEqual(मिदचोऽन्त्यात्परः_१_१_४७('म्', 'न्', 'वद्'), ('व', 'न्', 'द्'))

    def test_मिदचोऽन्त्यात्परः_१_१_४७_मुच्(self):
        self.assertEqual(मिदचोऽन्त्यात्परः_१_१_४७('म्', 'न्', 'मुच्'), ('मु', 'न्', 'च्'))


if __name__ == '__main__':
    unittest.main()
