#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.lasya import अचोऽन्त्यादि_टि_१_१_६४, आनय_तिङ्_प्रत्ययः, लस्य_३_४_७७

class TestLasya(unittest.TestCase):
    def test_आनय_तिङ्_प्रत्ययः_परस्मैपदम्(self):
        प्रत्ययाः = [['तिप्','तस्','झि'],
        		 ['सिप्','थस्','थ'],
                 ['मिप्','वस्','मस्']
        ]
        self.assertEqual([[आनय_तिङ्_प्रत्ययः(True, पुरुषः, वचनम्) for वचनम् in range(3)] for पुरुषः in range(3)], प्रत्ययाः)

    def test_आनय_तिङ्_प्रत्ययः_आत्मनेपदम्(self):
        प्रत्ययाः = [['त','आताम्','झ'],
        		 ['थास्','आथाम्','ध्वम्'],
                 ['इड्','वहि','महिङ्']
        ]
        self.assertEqual([[आनय_तिङ्_प्रत्ययः(False, पुरुषः, वचनम्) for वचनम् in range(3)] for पुरुषः in range(3)], प्रत्ययाः)

    def test_अचोऽन्त्यादि_टि_१_१_६४(self):
        self.assertEqual(अचोऽन्त्यादि_टि_१_१_६४('आथाम्'), 'आम्')

    def test_टित_आत्मनेपदानां_टेरे_३_४_७९(self):
        प्रत्ययाः = [['ते','आते','झे'],
        		 ['से','आथे','ध्वे'],
                 ['े','वहे','महे']
        ]
        self.assertEqual([[लस्य_३_४_७७('लट्', False, पुरुषः, वचनम्) for वचनम् in range(3)] for पुरुषः in range(3)], प्रत्ययाः)

if __name__ == '__main__':
    unittest.main()