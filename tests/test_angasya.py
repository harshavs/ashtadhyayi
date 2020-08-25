#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.angasya import आर्धधातुकस्येड्_वलादेः_७_२_३५, मिदेर्गुणः_७_३_८२
from ashtadhyayi.tinantarupam import तिङन्तरूपम्
from ashtadhyayi.lasya import लकारः


class TestAngaasya(unittest.TestCase):
    def test_पठ्_स्य(self):
        धातुः = {'धातुः': 'पठ्', 'सेट्': True}
        पदम् = तिङन्तरूपम्(धातुः, लकारः.लृट्, True, 0, 0)
        पदम्.विकरणप्रत्ययः = {'प्रत्ययः': 'स्य', 'आर्धधातुकम्': True}
        आर्धधातुकस्येड्_वलादेः_७_२_३५(पदम्)
        self.assertTrue(पदम्.विकरणप्रत्ययः['इडागमः'])

    def test_मिदेर्गुणः_७_३_८२(self):
        धातुः = {'धातुः': 'मिद्', 'सेट्': True}
        पदम् = तिङन्तरूपम्(धातुः, लकारः.लृट्, True, 0, 0)
        पदम्.विकरणप्रत्ययः = {'प्रत्ययः': 'स्य', 'आर्धधातुकम्': True}
        मिदेर्गुणः_७_३_८२(पदम्)
        self.assertTrue(पदम्.धातुः['आदेशः'] == 'मेद्')


if __name__ == '__main__':
    unittest.main()
