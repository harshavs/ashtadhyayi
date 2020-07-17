import unittest
from ashtadhyayi.tinantarupam import तिङन्तम्
from ashtadhyayi.lasya import लकारः


class TestTinantarupam(unittest.TestCase):

    def test_तिङन्तरूपम्_करोति(self):
        धातुः = {'धातुः': 'डुकृ॒ञ्', 'गणः': 'तनादिः'}
        करोति = तिङन्तम्(धातुः, लकारः.लोट्, True, 0, 0)
        self.assertTrue(करोति.तिङ्_प्रत्ययः['सार्वधातुकम्'])
        self.assertEqual(करोति.तिङ्_प्रत्ययः['प्रत्ययः'], 'तुप्')


if __name__ == '__main__':
    unittest.main()
