import re
from ashtadhyayi.pratyahara import वर्णाः


स्वरित = '\u0951'
अनुदात्त = '\u0952'


स्वरात्_स्वरमात्राः = {
                'अ': '',
                'आ': 'ा',
                'इ': 'ि',
                'ई': 'ी',
                'उ': 'ु',
                'ऊ': 'ू',
                'ऋ': 'ृ',
                'ॠ': 'ॄ',
                'ऌ': 'ॢ',
                'ए': 'े',
                'ऐ': 'ै',
                'ओ': 'ो',
                'औ': 'ौ',
                'अं': 'ं',
                'अः': 'ः'}

मात्राभ्यः_स्वराः = {
                '': 'अ',
                'ा': 'आ',
                'ि': 'इ',
                'ी': 'ई',
                'ु': 'उ',
                'ू': 'ऊ',
                'ृ': 'ऋ',
                'ॄ': 'ॠ',
                'ॢ': 'ऌ',
                'े': 'ए',
                'ै': 'ऐ',
                'ो': 'ओ',
                'ौ': 'औ',
                'ं': 'अं',
                'ः': 'अः'}


स्वरस्यदीर्घाः = {
                'अ': 'आ',
                '': 'ा',
                'इ': 'ई',
                'ि': 'ी',
                'उ': 'ऊ',
                'ु': 'ू',
                'ऋ': 'ॠ',
                'ृ': 'ॄ'}


स्वरस्यह्रस्वाः = {
                'आ': 'अ',
                'ा': '',
                'ई': 'इ',
                'ी': 'ि',
                'ऊ': 'उ',
                'ू': 'ु',
                'ॠ': 'ऋ',
                'ॄ': 'ृ'}


def स्वरात्_मात्रा(स्वराः):
    return ''.join(स्वरात्_स्वरमात्राः.get(स्वरः) or '' for स्वरः in स्वराः)


def मात्रायाः_स्वरः(मात्राः):
    return ''.join(मात्राभ्यः_स्वराः.get(मात्रा) or '' for मात्रा in मात्राः)


def स्वरमात्राः():
    return ''.join([स्वरमात्रा for स्वरमात्रा in स्वरात्_स्वरमात्राः.values()])


def स्वराः():
    return ''.join([स्वरमात्रा for स्वरमात्रा in स्वरात्_स्वरमात्राः.keys()])


def कु():
    return 'कखगघङ'


def चु():
    return 'चछजझञ'


def टु():
    return 'टठडढण'


def तु():
    return 'तथदधन'


def पु():
    return 'पफबभम'


def परसवर्णः(वर्णः):
    वर्गाः = [कु, चु, टु, तु, पु]
    for वर्गः in वर्गाः:
        वर्गः = वर्गः()
        if वर्णः in वर्गः:
            return वर्गः[4] + '्'


def दीर्घः(स्वरः):
    return स्वरस्यदीर्घाः.get(स्वरः)


def ह्रस्वः(स्वरः):
    return स्वरस्यह्रस्वाः.get(स्वरः)


def ह्रस्वाः():
    return list(स्वरस्यह्रस्वाः.values())


def दीर्घस्वराः():
    return list(स्वरस्यदीर्घाः.values())


def दीर्घाः(स्वराः):
    return ''.join(दी for स्वरः in स्वराः if (दी := दीर्घः(स्वरः)) is not None)


def दीर्घमात्राश्च(स्वराः):
    स्वराः += दीर्घाः(स्वराः)
    स्वराः += स्वरात्_मात्रा(स्वराः)
    return स्वराः


def हलन्तः(शब्दः):
    हल् = वर्णाः('हल्')
    हलन्तः = '[{हल्}]्$'.format(हल्=हल्)
    return bool(re.search(हलन्तः, शब्दः))


def अनुनासिकान्तः(शब्दः):
    ञम् = वर्णाः('ञम्')
    अनुनासिकान्तः = '[{ञम्}]्$'.format(ञम्=ञम्)
    return bool(re.search(अनुनासिकान्तः, शब्दः))
