#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.aardhadhatuka import आर्धधातुकस्येड्_वलादेः_७_२_३५, धात्वादेश
from ashtadhyayi.tinantarupam import तिङन्तरूपम्
from ashtadhyayi.lasya import लकारः


class TestAardhadhatuka(unittest.TestCase):
    def test_पठ्_स्य(self):
        धातुः = {'धातुः': 'पठ्', 'सेट्': True}
        पदम् = तिङन्तरूपम्(धातुः, लकारः.लृट्, True, 0, 0)
        पदम्.विकरणप्रत्ययः = {'प्रत्ययः': 'स्य', 'आर्धधातुकम्': True}
        self.assertEqual(आर्धधातुकस्येड्_वलादेः_७_२_३५(पदम्), 'पठिस्य')

    def test_अस्(self):
        धातुः = {'धातुः': 'अस्', 'सेट्': True}
        पदम् = तिङन्तरूपम्(धातुः, लकारः.लृट्, True, 0, 0)
        पदम्.विकरणप्रत्ययः = {'प्रत्ययः': 'सिप्', 'आर्धधातुकम्': True}
        धात्वादेश(पदम्)
        self.assertEqual(पदम्.धातुः['आदेशः'], 'भू')

    def test_ग्लै(self):
        धातुः = {'धातुः': 'ग्लै', 'सेट्': True}
        पदम् = तिङन्तरूपम्(धातुः, लकारः.लृट्, True, 0, 0)
        पदम्.विकरणप्रत्ययः = {'प्रत्ययः': 'सिप्', 'आर्धधातुकम्': True}
        धात्वादेश(पदम्)
        self.assertEqual(पदम्.धातुः['आदेशः'], 'ग्ला')


if __name__ == '__main__':
    unittest.main()
