import unittest
from ashtadhyayi.tinantarupam import तिङन्तम्, धात्वादेशः, धातुरूपम्
from ashtadhyayi.lasya import लकारः


class TestTinantarupam(unittest.TestCase):

    def test_तिङन्तरूपम्_करोति(self):
        धातुः = {'उपदेशः': 'डुकृ॒ञ्', 'गणः': 'तनादिः'}
        करोति = तिङन्तम्(धातुः, लकारः.लोट्, True, 0, 0)
        self.assertTrue(करोति.तिङ्_प्रत्ययः['सार्वधातुकम्'])
        self.assertEqual(करोति.तिङ्_प्रत्ययः['प्रत्ययः'], 'तुप्')

    def test_ग्लै(self):
        धातुः = {'उपदेशः': 'ग्लै', 'गणः': 'भ्वादिः', 'सेट्': True}
        पदम् = तिङन्तम्(धातुः, लकारः.लृट्, True, 0, 0)
        पदम्.विकरणप्रत्ययः = {'प्रत्ययः': 'सिप्', 'आर्धधातुकम्': True}
        धात्वादेशः(पदम्)
        self.assertEqual(पदम्.धातुः['आदेशः'], 'ग्ला')

    def test_कुर्दँ(self):
        धातुः = {'उपदेशः': 'कुर्दँ', 'गणः': 'भ्वादिः', 'सेट्': True}
        पदम् = तिङन्तम्(धातुः, लकारः.लृट्, True, 0, 0)
        पदम्.विकरणप्रत्ययः = {'प्रत्ययः': 'सिप्', 'आर्धधातुकम्': True}
        self.assertEqual(पदम्.धातुः['धातुः'], 'कूर्द्')

    def test_वृजीँ(self):
        धातुः = {'उपदेशः': 'वृजीँ', 'गणः': 'चुरादिः', 'सेट्': True}
        पदम् = तिङन्तम्(धातुः, लकारः.लृट्, True, 0, 0)
        पदम्.विकरणप्रत्ययः = {'प्रत्ययः': 'सिप्', 'आर्धधातुकम्': True}
        self.assertEqual(पदम्.धातुः['धातुः'], 'वृज्')

    def test_ष्टुचँ॒(self):
        धातुः = {'उपदेशः': 'ष्टुचँ॒', 'गणः': 'भ्वादिः', 'सेट्': True}
        पदम् = तिङन्तम्(धातुः, लकारः.लृट्, True, 0, 0)
        पदम्.विकरणप्रत्ययः = {'प्रत्ययः': 'सिप्', 'आर्धधातुकम्': True}
        self.assertEqual(पदम्.धातुः['धातुः'], 'स्टुच्')

    # TODO: separate file
    def test_धातुरूपम्(self):
        count = 0
        results = []
        errors = []
        with open('tests/dhaatupaatha.txt') as dhaatupatha:
            for dhaatu in dhaatupatha:
                #print(count)
                count += 1
                # Skip first two lines
                if count > 2:
                    dhaatu = dhaatu.split(',')
                    dhaatu[8] = dhaatu[8].replace('\n', '')
                    upadesha = dhaatu[2].replace(' ', '')
                    upadesha = upadesha.split('(')
                    upadesha[1] = upadesha[1].replace(')', '')
                    dhaatu[2] = upadesha
                    try:
                        results.append(धातुरूपम्(dhaatu[2][0], dhaatu[1]))
                    except Exception as e:
                        errors.append(str(count) + 'Failed at '+str(dhaatu)+' with '+str(e))
        with open('tinresults.json', 'w+') as tinfile:
            tinfile.write(str(results))
            tinfile.write(str(errors))


if __name__ == '__main__':
    unittest.main()
