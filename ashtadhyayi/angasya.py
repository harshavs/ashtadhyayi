#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ashtadhyayi.pratyahara import वल्, वर्णाः
from ashtadhyayi.utils import स्वरात्_मात्रा, मात्रायाः_स्वरः, दीर्घाः, ह्रस्वः, दीर्घः
from ashtadhyayi.sajna import इको_गुणवृद्धी_१_१_३, अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५
import re
from ashtadhyayi.aakadaaraat_ekaa_sajna import लघु_वा
from ashtadhyayi.it_samjna_prakarana import कित्_वा, ङित्_वा


def अङ्गस्य_६_४_१(पदम्):
    हलः_६_४_२(पदम्)


def हलः_६_४_२(पदम्):
    सम्प्रसारणम् = पदम्.धातुः['सम्प्रसारणम्']
    if सम्प्रसारणम्:
        पदम्.धातुः['सम्प्रसारणम्'] = दीर्घः(सम्प्रसारणम्)


def नामि_६_४_३(पदम्):
    # TODO sup pratyaya
    pass


def न_तिसृचतसृ_६_४_४(पदम्):
    # TODO
    pass


def छन्दस्युभयथा_६_४_५(पदम्):
    pass


def नृ_च_६_४_६(पदम्):
    pass


def नोपधायाः_६_४_७(पदम्):
    pass


def सर्वनामस्थाने_चासम्बुद्धौ_६_४_८(पदम्):
    pass


def वा_षपूर्वस्य_निगमे_६_४_९(पदम्):
    pass


def सान्तमहतः_संयोगस्य_६_४_१०(पदम्):
    pass


def अप्तृन्तृच्स्वसृनप्तृनेष्टृत्वष्टृक्षत्तृहोतृपोतृप्रशास्तॄणाम्_६_४_११(पदम्):
    pass


def इन्हन्पूषार्यम्णां_शौ_६_४_१२(पदम्):
    pass


def सौ_च_६_४_१३(पदम्):
    pass


def अत्वसन्तस्य_चाधातोः_६_४_१४(पदम्):
    pass


def अनुनासिकस्य_क्विझलोः_क्ङिति_६_४_१५(पदम्):
    धातुः = पदम्.धातुः['धातुः']
    if धातुः[-2] in वर्णाः('ञम्'):
        प्रत्ययः = पदम्.कृत्प्रत्ययः['प्रत्ययः']
        if प्रत्ययः == 'क्विप्' or झलोः_क्ङिति(प्रत्ययः):
            उपधा = अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५(धातुः)
            पदम्.धातुः['धातुः'] = धातुः.replace(उपधा, दीर्घः(उपधा))


def झलोः_क्ङिति(प्रत्ययः):
    return प्रत्ययः[0] in वर्णाः('झल्') and (ङित्_वा(प्रत्ययः) or कित्_वा(प्रत्ययः))


def अज्झनगमां_सनि_६_४_१६(पदम्):
    धातुः = पदम्.धातुः['धातुः']
    प्रत्ययः = पदम्.कृत्प्रत्ययः['प्रत्ययः']
    return (धातुः[-2] in वर्णाः('अच्') or धातुः in ['हन्', 'गम्']) and (झलोः_क्ङिति(प्रत्ययः) or प्रत्ययः == 'सन्')


def तनोतेर्विभाषा_६_४_१७(पदम्):
    # TODO tanoti
    return पदम्.धातुः['धातुः'] == ''


def क्रमश्च_क्त्वि_६_४_१८(पदम्):
    # TODO
    return ''


def च्छ्वोः_शूडनुनासिके_च_६_४_१९(पदम्):
    # TODO
    return ''


def झोऽन्तः_७_१_३(पदम्):
    प्रत्ययः = पदम्.तिङ्_प्रत्ययः['प्रत्ययः']
    if 'झ' in प्रत्ययः:
        पदम्.तिङ्_प्रत्ययः['प्रत्ययः'] = प्रत्ययः.replace('झ', 'अन्त')


def इदितो_नुम्_धातोः_७_१_५८(पदम्):
    if पदम्.धातुः['इत्'] == 'इँ':
        पदम्.धातुः['आगमः'] = 'नुम्'


def नेड्_वशि_कृति_७_२_८(पदम्):
    # TODO
    return None


def तितुत्रतथसिसुसरकसेषु_च_७_२_९(पदम्):
    # TODO
    return None


def एकाच_उपदेशेऽनुदात्तात्_७_२_१०(पदम्):
    # TODO
    return None


def श्र्युकः_किति_७_२_११(पदम्):
    # TODO
    return None


def सनि_ग्रहगुहोश्च_७_२_१२(पदम्):
    # TODO
    return None


def कृसृभृवृस्तुद्रुस्रुश्रुवो_लिटि_७_२_१३(पदम्):
    # TODO
    return None


def श्वीदितो_निष्ठायाम्_७_२_१४(पदम्):
    # TODO
    return None


def यस्य_विभाषा_७_२_१५(पदम्):
    # TODO
    return None


def आदितश्च_७_२_१६(पदम्):
    # TODO
    return None


def विभाषा_भावादिकर्मणोः_७_२_१७(पदम्):
    # TODO
    return None


def क्षुब्धस्वान्तध्वान्तलग्नम्लिष्टविरिब्धफाण्टबाढानि_मन्थमनस्तमःसक्ताविस्पष्टस्वरानायासभृशेषु_७_२_१८(पदम्):
    # TODO
    return None


def धृषिशसी_वैयात्ये_७_२_१९(पदम्):
    # TODO
    return None


def दृढः_स्थूलबलयोः_७_२_२०(पदम्):
    # TODO
    return None


def प्रभौ_परिवृढः_७_२_२१(पदम्):
    # TODO
    return None


def कृच्छ्रगहनयोः_कषः_७_२_२२(पदम्):
    # TODO
    return None


def घुषिरविशब्दने_७_२_२३(पदम्):
    # TODO
    return None


def अर्देः_संनिविभ्यः_७_२_२४(पदम्):
    # TODO
    return None


def अभेश्चाविदूर्ये_७_२_२५(पदम्):
    # TODO
    return None


def णेरध्ययने_वृत्तम्_७_२_२६(पदम्):
    # TODO
    return None


def वा_दान्तशान्तपूर्णदस्तस्पष्टच्छन्नज्ञप्ताः_७_२_२७(पदम्):
    # TODO
    return None


def रुष्यमत्वरसंघुषास्वनाम्_७_२_२८(पदम्):
    # TODO
    return None


def हृषेर्लोमसु_७_२_२९(पदम्):
    # TODO
    return None


def अपचितश्च_७_२_३०(पदम्):
    # TODO
    return None


def ह्रु_ह्वरेश्छन्दसि_७_२_३१(पदम्):
    # TODO
    return None


def अपरिह्वृताश्च_७_२_३२(पदम्):
    # TODO
    return None


def सोमे_ह्वरितः_७_२_३३(पदम्):
    # TODO
    return None


def ग्रसितस्कभितस्तभितोत्तभितचत्तविकस्तविशस्तॄशंस्तृशास्तृतरुतृतरूतृवरुतृवरूतृवरुत्रीरुज्ज्वलितिक्षरितिक्षमितिवमित्यमितीति_च_७_२_३४(पदम्):  # noqa: E501
    # TODO
    return None


def आर्धधातुकस्येड्_वलादेः_७_२_३५(पदम्):
    if पदम्.धातुः.get('सेट्') and पदम्.विकरणप्रत्ययः['आर्धधातुकम्']:
        आर्धधातुक_विकरण_सेट्_प्रत्ययः = पदम्.विकरणप्रत्ययः['प्रत्ययः']
        पदम्.विकरणप्रत्ययः['इडागमः'] = आर्धधातुक_विकरण_सेट्_प्रत्ययः and वल्(आर्धधातुक_विकरण_सेट्_प्रत्ययः[0])

# सेट्धातुः = पदम्.धातुः['धातुः']
# return सेट्धातुः[:-1] + 'ि' + आर्धधातुक_विकरण_सेट्_प्रत्ययः
# else:
#     return सेट्धातुः[:-1] + आर्धधातुक_विकरण_सेट्_प्रत्ययः


def मिदेर्गुणः_७_३_८२(पदम्):
    धातुः = पदम्.धातुः['धातुः']
    if धातुः == 'मिद्' or सार्वधातुकार्धधातुकयोः_७_३_८४(पदम्) or पुगन्तलघूपधस्य_च_७_३_८६(पदम्):
        इकः_गुणः(पदम्)


# TODO move this to an appropriate place
def इकः_गुणः(पदम्):
    धातुः = पदम्.धातुः['धातुः']
    इक् = वर्णाः('इक्')
    इक् += स्वरात्_मात्रा(इक्)
    इक्_दीर्घाः = दीर्घाः(इक्)
    इक् += इक्_दीर्घाः
    हल् = वर्णाः('हल्')
    इकः = '^(?:[{हल्}]*)([{इक्}])'.format(हल्=हल्, इक्=इक्)
    स्वरः = re.search(इकः, धातुः)
    if स्वरः:
        स्वरः = स्वरः.group(1)
        अच् = वर्णाः('अच्')

        if स्वरः in इक्_दीर्घाः:
            इक् = ह्रस्वः(स्वरः)
        else:
            इक् = स्वरः

        if इक् not in अच्:
            गुणः = स्वरात्_मात्रा(इको_गुणवृद्धी_१_१_३(मात्रायाः_स्वरः(इक्)))
        else:
            गुणः = इको_गुणवृद्धी_१_१_३(इक्)

        पदम्.धातुः['आदेशः'] = धातुः.replace(स्वरः, गुणः)


def जुसि_च_७_३_८३(पदम्):
    # TODO
    pass


def सार्वधातुकार्धधातुकयोः_७_३_८४(पदम्):
    return पदम्.विकरणप्रत्ययः['सार्वधातुकम्'] or पदम्.विकरणप्रत्ययः['आर्धधातुकम्']


def पुगन्तलघूपधस्य_च_७_३_८६(पदम्):
    return पदम्.धातुः.get('आगमः') == 'पुक्' or लघु_वा(अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५(पदम्.धातुः['धातुः']))


def अतो_दीर्घो_यञि_७_३_१०१(रू, प्रत्ययः):
    if प्रत्ययः[0] in वर्णाः('यञ्') and रू[-1] in वर्णाः('हल्'):
        रू += 'ा'
    return रू
