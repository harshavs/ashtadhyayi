#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.it_samjna_prakarana import इत्संज्ञाप्रकरणम्, उपदेशसंज्ञकः

class TestItSamjnaPrakarana(unittest.TestCase):
    def test_गम्ऌँ(self):
        self.assertEqual(इत्संज्ञाप्रकरणम्('गम्ऌँ', उपदेशसंज्ञकः.धातुः), 'ग')

    def test_शप्(self):
        self.assertEqual(इत्संज्ञाप्रकरणम्('शप्'), 'श')

    def test_शप्(self):
        self.assertEqual(इत्संज्ञाप्रकरणम्('अम्', उपदेशसंज्ञकः.प्रत्ययः, True), 'अम्')
    
    # def test_टुक्षु(self):
    #     self.assertEqual(इत्संज्ञाप्रकरणम्('टुक्षु'), उपदेशसंज्ञकः.धातुः, 'क्षु')

    def test_डुकृञ्(self):
        self.assertEqual(इत्संज्ञाप्रकरणम्('डुकृञ्', उपदेशसंज्ञकः.धातुः), 'कृ')

    def test_ष्यङ्(self):
        self.assertEqual(इत्संज्ञाप्रकरणम्('ष्यङ्', उपदेशसंज्ञकः.प्रत्ययः), 'य')

    def test_च्फ(self):
        self.assertEqual(इत्संज्ञाप्रकरणम्('च्फ', उपदेशसंज्ञकः.प्रत्ययः), 'फ')

    def test_ल्युट्(self):
        self.assertEqual(इत्संज्ञाप्रकरणम्('ल्युट्', उपदेशसंज्ञकः.प्रत्ययः), 'यु')
     

if __name__ == '__main__':
    unittest.main()