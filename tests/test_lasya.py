#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.lasya import लस्य_३_४_७७

class TestLasya(unittest.TestCase):
    def test_परस्मैपदम्(self):
        प्रत्ययाः = [['तिप्','तस्','झि'],
        		 ['सिप्','थस्','थ'],
                 ['मिप्','वस्','मस्']
        ]
        self.assertEqual([[लस्य_३_४_७७('लट्', True, पुरुषः, वचनम्) for वचनम् in range(3)] for पुरुषः in range(3)], प्रत्ययाः)

    def test_आत्मनेपदम्(self):
        प्रत्ययाः = [['त','आताम्','झ'],
        		 ['थास्','आथाम्','ध्वम्'],
                 ['इड्','वहि','महिङ्']
        ]
        self.assertEqual([[लस्य_३_४_७७('लट्', False, पुरुषः, वचनम्) for वचनम् in range(3)] for पुरुषः in range(3)], प्रत्ययाः)

    def test_टित_आत्मनेपदानां_टेरे_३_४_७९(self):
        self.assertEqual(लस्य_३_४_७७('लट्', False, 0 , 0), 'ते')

if __name__ == '__main__':
    unittest.main()
