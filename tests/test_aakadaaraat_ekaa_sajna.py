#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.aakadaaraat_ekaa_sajna import ह्रस्वं_लघु_१_४_१०, संयोगे_गुरु_१_४_११, दीर्घं_च_१_४_१२, लघु_गुरु


class TestAakadaraatEkaaSajna(unittest.TestCase):
    def test_ह्रस्वं_लघु_१_४_१०_अग्नि(self):
        self.assertEqual(ह्रस्वं_लघु_१_४_१०('अग्नि').group(), 'अ')

    def test_ह्रस्वं_लघु_१_४_१०_हरि(self):
        self.assertEqual(ह्रस्वं_लघु_१_४_१०('हरि').group(), 'ह')

    def test_संयोगे_गुरु_१_४_११_अग्नि(self):
        self.assertEqual(संयोगे_गुरु_१_४_११('अग्नि'), True)

    def test_संयोगे_गुरु_१_४_११_हरि(self):
        self.assertEqual(संयोगे_गुरु_१_४_११('हरि'), False)

    def test_दीर्घं_च_१_४_१२_राजा(self):
        self.assertEqual(दीर्घं_च_१_४_१२('राजा').group(), 'ा')

    def test_दीर्घं_च_१_४_१२_हरि(self):
        self.assertIsNone(दीर्घं_च_१_४_१२('हरि'))

    def test_लघु_गुरु(self):
        result = लघु_गुरु("""धर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः।
                         मामकाः पाण्डवाश्चैव किमकुर्वत सञ्जय""")
        self.assertEqual(result, [
            False, False, False, False, True, False, False, False,
            True, True, False, False, True, False, True, False,
            False, True, False, False, True, False, False, True,
            True, True, False, True, True, False, True, True
        ])


if __name__ == '__main__':
    unittest.main()
