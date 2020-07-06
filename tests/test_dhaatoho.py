import unittest
from ashtadhyayi.dhaatoho import सार्वधातुकम्_आर्धधातुकम्
from ashtadhyayi.tinantarupam import तिङन्तरूपम्
from ashtadhyayi.lasya import लकारः


class TestDhaatoho(unittest.TestCase):

    def test_सार्वधातुकम्_आर्धधातुकम्_तिप्(self):
        तिप् = तिङन्तरूपम्('पदँ', लकारः.लोट्, True, 0, 0)
        तिप्.तिङ्_प्रत्ययः['प्रत्ययः'] = 'तिप्'
        सार्वधातुकम्_आर्धधातुकम्(तिप्)
        self.assertTrue(तिप्.तिङ्_प्रत्ययः['सार्वधातुकम्'])


if __name__ == '__main__':
    unittest.main()
