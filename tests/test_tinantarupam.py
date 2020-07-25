import unittest
from ashtadhyayi.tinantarupam import तिङन्तम्, तिङन्तरूपम्, धात्वादेशः
from ashtadhyayi.lasya import लकारः


class TestTinantarupam(unittest.TestCase):

    def test_तिङन्तरूपम्_करोति(self):
        धातुः = {'धातुः': 'डुकृ॒ञ्', 'गणः': 'तनादिः'}
        करोति = तिङन्तम्(धातुः, लकारः.लोट्, True, 0, 0)
        self.assertTrue(करोति.तिङ्_प्रत्ययः['सार्वधातुकम्'])
        self.assertEqual(करोति.तिङ्_प्रत्ययः['प्रत्ययः'], 'तुप्')

    def test_ग्लै(self):
        धातुः = {'धातुः': 'ग्लै', 'सेट्': True}
        पदम् = तिङन्तरूपम्(धातुः, लकारः.लृट्, True, 0, 0)
        पदम्.विकरणप्रत्ययः = {'प्रत्ययः': 'सिप्', 'आर्धधातुकम्': True}
        धात्वादेशः(पदम्)
        self.assertEqual(पदम्.धातुः['आदेशः'], 'ग्ला')


if __name__ == '__main__':
    unittest.main()
