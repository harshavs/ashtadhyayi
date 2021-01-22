#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ashtadhyayi.pratyahara import वल्, वर्णाः
from ashtadhyayi.utils import स्वरात्_मात्रा, मात्रायाः_स्वरः, दीर्घाः, ह्रस्वः, दीर्घः
from ashtadhyayi.sajna import इको_गुणवृद्धी_१_१_३, अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५
import re
from ashtadhyayi.aakadaaraat_ekaa_sajna import लघु_वा


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
