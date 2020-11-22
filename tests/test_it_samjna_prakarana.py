import unittest
from ashtadhyayi.it_samjna_prakarana import इत्, उपदेशसंज्ञकः


class TestItSamjnaPrakarana(unittest.TestCase):

    def test_गम्ऌँ(self):
        self.assertEqual(इत्('गम्ऌँ', उपदेशसंज्ञकः.धातुः)['उपदेशः'], 'गम्')

    def test_शप्(self):
        self.assertEqual(इत्('शप्')['उपदेशः'], 'अ')

    def test_अम्(self):
        self.assertEqual(इत्('अम्', उपदेशसंज्ञकः.प्रत्ययः, True)['उपदेशः'], 'अम्')

    def test_टुक्षु(self):
        self.assertEqual(इत्('टुक्षु', उपदेशसंज्ञकः.धातुः)['उपदेशः'], 'क्षु')

    def test_डुकृञ्(self):
        self.assertEqual(इत्('डुकृञ्', उपदेशसंज्ञकः.धातुः)['उपदेशः'], 'कृ')

    def test_ष्यङ्(self):
        self.assertEqual(इत्('ष्यङ्', उपदेशसंज्ञकः.प्रत्ययः)['उपदेशः'], 'य')

    def test_च्फ(self):
        self.assertEqual(इत्('च्फ', उपदेशसंज्ञकः.प्रत्ययः)['उपदेशः'], 'फ')

    def test_ल्युट्(self):
        self.assertEqual(इत्('ल्युट्', उपदेशसंज्ञकः.प्रत्ययः)['उपदेशः'], 'यु')

    def test_झ(self):
        self.assertEqual(इत्('झ', उपदेशसंज्ञकः.प्रत्ययः)['उपदेशः'], 'अ')

    def test_णल्(self):
        self.assertEqual(इत्('णल्', उपदेशसंज्ञकः.प्रत्ययः)['उपदेशः'], 'अ')


if __name__ == '__main__':
    unittest.main()
