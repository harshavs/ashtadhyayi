import unittest
from ashtadhyayi.tinantarupam import तिङन्तम्, धात्वादेशः
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

    def test_कृ(self):
        results = {}
        padis = [True, False]
        # with open('tests/dhaatupaatha.txt') as dhaatupatha:
        धातुः = {'उपदेशः': 'डुकृ॒ञ्', 'गणः': 'तनादिः'}
        purushas = ['प्रथमपुरुषः', 'मध्यमपुरुषः', 'उत्तमपुरुषः']
        vachanas = ['एकवचनम्', 'द्विवचनम्', 'बहुवचनम्']
        for padi in padis:
            results[padi] = {}
            padiresult = results[padi]
            for ल in लकारः:
                padiresult[str(ल)] = {}
                lresult = padiresult[str(ल)]
                for purusha in range(0, 3):
                    p = purushas[purusha]
                    lresult[p] = {}
                    presult = lresult[p]
                    for vachana in range(0, 3):
                        v = vachanas[vachana]
                        presult[v] = str(तिङन्तम्(धातुः, ल, padi, purusha, vachana))
        # print(results)
        with open('tinresults.json', 'w+') as tinfile:
            tinfile.write(str(results))


if __name__ == '__main__':
    unittest.main()
