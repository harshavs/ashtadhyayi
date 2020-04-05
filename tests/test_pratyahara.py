#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ashtadhyayi.pratyahara import वर्णाः

class TestPratyahara(unittest.TestCase):
    def test_प्रत्याहारः(self):
        f = open('tests/pratyahara_output.txt')
        pratyaharas = f.readlines()
        for pratyahara in pratyaharas:
            pratyahara = pratyahara.split(' ')
            self.assertEqual(वर्णाः(pratyahara[0]), pratyahara[1][:-1])
        f.close()

if __name__ == '__main__':
    unittest.main()