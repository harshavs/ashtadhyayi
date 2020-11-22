from enum import Enum
import re
from ashtadhyayi.pratyahara import वर्णाः
from ashtadhyayi.utils import स्वरात्_मात्रा, अनुदात्त, स्वरित, स्वरस्यदीर्घाः


उपदेशसंज्ञकः = Enum('उपदेशसंज्ञकः', 'प्रत्याहारः प्रत्ययः आदेशः आगमः धातुः')


def उपदेशेऽजनुनासिक_इत्_१_३_२():
    अच् = वर्णाः('अच्')
    अच् += ''.join([स्वरस्यदीर्घाः.get(स्वर) for स्वर in अच् if स्वरस्यदीर्घाः.get(स्वर) is not None])
    हल् = वर्णाः('हल्')
    अजनुनासिक = []
    स्वरमात्रा = '[{अच्}][{अनुदात्त}{स्वरित}]?ँ[{अनुदात्त}{स्वरित}]?'
    अजनुनासिक.append(स्वरमात्रा.format(अच्=अच्, अनुदात्त=अनुदात्त, स्वरित=स्वरित))
    अजनुनासिक.append((स्वरमात्रा.format(अच्=स्वरात्_मात्रा(अच्), अनुदात्त=अनुदात्त, स्वरित=स्वरित),  '्', ''))
    हल = '(?<=[{हल्}])([{अनुदात्त}{स्वरित}]?ँ[{अनुदात्त}{स्वरित}]?)'
    अजनुनासिक.append((हल.format(हल्=हल्, अनुदात्त=अनुदात्त, स्वरित=स्वरित), '्', 'अ'))
    return अजनुनासिक


def हलन्त्यम्_१_३_३():
    return हलन्त्यम्()


def हलन्त्यम्(विभक्तौ=''):
    हल् = वर्णाः('हल्')
    हल् = "".join([वर्णः for वर्णः in हल् if वर्णः not in विभक्तौ])
    return '[{हल्}]्$'.format(हल्=हल्)


def न_विभक्तौ_तुस्माः_१_३_४():
    return हलन्त्यम्('तथदधनसम')


def आदिर्ञिटुडवः_१_३_५():
    आदिर्ञिटुडवः = '^(ञि|टु|डु)'
    return आदिर्ञिटुडवः


def षः_प्रत्ययस्य_१_३_६():
    षः = []
    षः.append('^ष्')
    षः.append(('^ष', 'अ', ''))
    return षः


def चुटू_१_३_७():
    चुटू = '^[चछजझञटठडढण]्?'
    return चुटू


def लशक्वतद्धिते_१_३_८():
    लशकु = '^[लशकखगघङ]्?'
    return लशकु


def तस्य_लोपः_१_३_९(इत्, उपदेशः, replacement=''):
    # '' = लोपः
    return उपदेशः.replace(इत्, replacement)


def इत्संज्ञासूत्राणि(उपदेशः, उपदेशसंज्ञकः=उपदेशसंज्ञकः.प्रत्ययः, विभक्तिः=False):
    सूत्राणि = []

    # अजनुनासिक
    सूत्राणि.append(उपदेशेऽजनुनासिक_इत्_१_३_२())

    # हलन्त्यम्
    if not विभक्तिः:
        सूत्राणि.append(हलन्त्यम्_१_३_३())
    else:
        सूत्राणि.append(न_विभक्तौ_तुस्माः_१_३_४())

    # आदिर्ञिटुडवः
    सूत्राणि.append(आदिर्ञिटुडवः_१_३_५())

    if उपदेशसंज्ञकः == उपदेशसंज्ञकः.प्रत्ययः:
        # षः_प्रत्ययस्य_१_३_६
        सूत्राणि.append(षः_प्रत्ययस्य_१_३_६())

        # चुटू
        सूत्राणि.append(चुटू_१_३_७())

        # लशक्वतद्धिते
        सूत्राणि.append(लशक्वतद्धिते_१_३_८())
    return सूत्राणि


# TODO do I need this?
# def इत्संज्ञाप्रकरणम्(उपदेशः, उपदेशसंज्ञकः=उपदेशसंज्ञकः.प्रत्ययः, विभक्तिः=False):
#     सूत्राणि = इत्संज्ञासूत्राणि(उपदेशः, उपदेशसंज्ञकः, विभक्तिः)
#     for सूत्रम् in सूत्राणि:
#         उपदेशः = तस्य_लोपः_१_३_९(सूत्रम्, उपदेशः)

#     # if there are no chars left in the string,
#     # then it means it is अ as a consonant has अ but no character for it
#     if उपदेशः == '':
#         उपदेशः = 'अ'

#     # if anunasika exists even after ith, then it is of अ
#     if 'ँ' in उपदेशः:
#         उपदेशः = उपदेशः.replace('ँ', '्')
#     return उपदेशः


def इत्(उपदेशः, उपदेशसंज्ञकः=उपदेशसंज्ञकः.प्रत्ययः, विभक्तिः=False):
    सूत्राणि = इत्संज्ञासूत्राणि(उपदेशः, उपदेशसंज्ञकः, विभक्तिः)
    इत् = []
    matches = []
    for सूत्रम् in सूत्राणि:
        if type(सूत्रम्) is list:
            for सूत्र in सूत्रम्:
                sutra = सूत्र
                prefix = ''
                replacement = ''
                if type(सूत्र) is tuple:
                    replacement = सूत्र[1]
                    sutra = सूत्र[0]
                    prefix = सूत्र[2]

                match = re.search(sutra, उपदेशः)
                if match and उपदेशः:
                    इत्.append(prefix + match.group())
                    matches.append((match.group(), replacement))
        else:
            match = re.search(सूत्रम्, उपदेशः)
            if match and उपदेशः:
                इत्.append(match.group())
                matches.append((match.group(), ''))

    for match in matches:
        उपदेशः = तस्य_लोपः_१_३_९(match[0], उपदेशः, match[1])
    # if there are no chars left in the string,
    # then it means it is अ as a consonant has अ but no character for it
    if उपदेशः == '':
        उपदेशः = 'अ'

    # # if anunasika exists even after ith, then it is of अ
    # अनुदात्त_अनुनासिक = '{अनुदात्त}'.format(अनुदात्त=अनुदात्त)
    # # anudatta prefixed
    # उपदेशः = replace_anunasikaswara(अनुदात्त_अनुनासिक, '', उपदेशः, इत्)

    # # anudatta suffixed
    # उपदेशः = replace_anunasikaswara('', अनुदात्त_अनुनासिक, उपदेशः, इत्)

    # उदात्त_अनुनासिक = '{उदात्त}'.format(उदात्त=उदात्त)

    # # udatta prefixed
    # उपदेशः = replace_anunasikaswara(उदात्त_अनुनासिक, '', उपदेशः, इत्)

    # # udatta suffixed
    # उपदेशः = replace_anunasikaswara('', उदात्त_अनुनासिक, उपदेशः, इत्)

    # # just anunasika
    # उपदेशः = replace_anunasikaswara('', '', उपदेशः, इत्)

    return {'उपदेशः': उपदेशः, 'इत्': इत्}


# TODO find a better way. also udatta & anudata after anunasika or before?
def replace_anunasikaswara(prev, after, उपदेशः, इत्):
    अनुनासिक = prev + 'ँ' + after
    if अनुनासिक in उपदेशः:
        उपदेशः = उपदेशः.replace(अनुनासिक, '्')
        इत्.append('अ'+अनुनासिक)
    return उपदेशः


def शित्_वा(प्रत्ययः):
    return इत्(प्रत्ययः, उपदेशसंज्ञकः.प्रत्ययः)['इत्'][0] == 'श्'


def टित्_वा(लकारः):
    return इत्(लकारः, उपदेशसंज्ञकः.आदेशः)['इत्'][0] == 'ट्'


def ङित्_वा(लकारः):
    return इत्(लकारः, उपदेशसंज्ञकः.आदेशः)['इत्'][0] == 'ङ्'


def ञित्_वा(लकारः):
    return इत्(लकारः, उपदेशसंज्ञकः.आदेशः)['इत्'][0] == 'ञ्'


def णित्_वा(लकारः):
    return इत्(लकारः, उपदेशसंज्ञकः.आदेशः)['इत्'][0] == 'ण्'


def कित्_वा(प्रत्ययः):
    return 'क्' in इत्(प्रत्ययः, उपदेशसंज्ञकः.प्रत्ययः)['इत्']
