#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.angasya import आर्धधातुकस्येड्_वलादेः_७_२_३५
from ashtadhyayi.tinantarupam import तिङन्तरूपम्
from ashtadhyayi.lasya import लकारः


class TestAngaasya(unittest.TestCase):
    def test_पठ्_स्य(self):
        धातुः = {'धातुः': 'पठ्', 'सेट्': True}
        पदम् = तिङन्तरूपम्(धातुः, लकारः.लृट्, True, 0, 0)
        पदम्.विकरणप्रत्ययः = {'प्रत्ययः': 'स्य', 'आर्धधातुकम्': True}
        आर्धधातुकस्येड्_वलादेः_७_२_३५(पदम्)
        self.assertTrue(पदम्.विकरणप्रत्ययः['इडागमः'])


if __name__ == '__main__':
    unittest.main()
