# from ashtadhyayi.it_samjna_prakarana import उपदेशसंज्ञकः, इत्
# from ashtadhyayi.sajna import अनुदात्तङित_आत्मनेपदम्_१_३_१२, स्वरितञितः_कर्त्रभिप्राये_क्रियाफले_१_३_७२
# from ashtadhyayi.utils import स्वरित, अनुदात्त
# from ashtadhyayi.dhaatoho import सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो_णिच्_३_१_२५
import unittest


class TestDhaatupatha(unittest.TestCase):
    def test_dhaatupatha(self):
        # with open('tests/dhaatupaatha.txt') as dhaatupatha:
        #     count = 0
        #     acount = 0
        #     ucount = 0
        #     dcount = 0
        #     ap = 0
        #     up = 0
        #     pp = 0
        #     dset = set()
        #     ds = []
        #     for dhaatu in dhaatupatha:
        #         # Skip first two lines
        #         if count < 2:
        #             count += 1
        #         elif count < 7000:
        #             count += 1
        #             dhaatu = dhaatu.split(',')
        #             dhaatu[8] = dhaatu[8].replace('\n', '')
        #             upadesha = dhaatu[2].replace(' ', '')
        #             upadesha = upadesha.split('(')
        #             upadesha[1] = upadesha[1].replace(')', '')
        #             dhaatu[2] = upadesha
        #             dhaatu.append(इत्(dhaatu[2][0], उपदेशसंज्ञकः.धातुः))
        #             if dhaatu[5] == 'आ.प':
        #                 ap += 1
        #             elif dhaatu[5] == 'उ.प':
        #                 up += 1
        #             elif dhaatu[5] == 'प.प':
        #                 pp += 1
        #             else:
        #                 raise AssertionError()

        #             if स्वरितञितः_कर्त्रभिप्राये_क्रियाफले_१_३_७२(dhaatu[9]['इत्'])
        #             or सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो_णिच्_३_१_२५(dhaatu[1]):
        #                 if dhaatu[5] == 'उ.प':
        #                     ucount += 1
        #                 else:
        #                     print(dhaatu)
        #                     ds.append(dhaatu)

        #             if dhaatu[5] == 'उ.प' and not स्वरितञितः_कर्त्रभिप्राये_क्रियाफले_१_३_७२(dhaatu[9]['इत्']):
        #                 if not सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो_णिच्_३_१_२५(dhaatu[1]):
        #                     # print(dhaatu)
        #                     ds.append(dhaatu)
        #                 # if dhaatu[5] == 'आ.प':
        #                 #     acount += 1
        #                 # else:
        #                 #     print(dhaatu)

        #             if अनुदात्तङित_आत्मनेपदम्_१_३_१२(dhaatu[9]['इत्']):
        #                 #print(dhaatu)
        #                 #ds.append(dhaatu)
        #                 if dhaatu[5] == 'आ.प':
        #                     acount += 1
        #                 else:
        #                     print(dhaatu)

        #             upadesa = dhaatu[9]['उपदेशः'].replace(अनुदात्त, '')
        #             upadesa = upadesa.replace(स्वरित, '')

        #             if upadesa != dhaatu[2][1]:
        #                 ds.apgitpend(dhaatu)
        #     print("ubhayapadi"+str(ucount))
        #     print("aatmanepadi"+str(acount))
        #     print(f"ap:{str(ap)}:up:{str(up)}:pp:{str(pp)}")
        #     print(len(dset))
        #     print(dcount)
        #     print(count)
        #     with open('nit.txt', 'w+') as nit:
        #         for d in ds:
        #             nit.write(str(d)+'\n')
        #         # nit.write(str(hex(ord(u'अ॑जँ॑'[1]))))
        #         print(str(hex(ord(u'अँ॑'[2]))))
        pass
