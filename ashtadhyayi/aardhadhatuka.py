#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ashtadhyayi.pratyahara import वर्णाः


def नेड्_वशि_कृति_७_२_८(पदम्):
    # TODO
    return None


def तितुत्रतथसिसुसरकसेषु_च_७_२_९(पदम्):
    # TODO
    return None


def आर्धधातुकस्येड्_वलादेः_७_२_३५(पदम्):
    if पदम्.धातुः.get('सेट्') and पदम्.विकरणप्रत्ययः['आर्धधातुकम्']:
        सेट्धातुः = पदम्.धातुः['धातुः']
        आर्धधातुक_विकरण_सेट्_प्रत्ययः = पदम्.विकरणप्रत्ययः['प्रत्ययः']
        if वल्(आर्धधातुक_विकरण_सेट्_प्रत्ययः[0]):
            return सेट्धातुः[:-1] + 'ि' + आर्धधातुक_विकरण_सेट्_प्रत्ययः
        else:
            return सेट्धातुः[:-1] + आर्धधातुक_विकरण_सेट्_प्रत्ययः


def वल्(वर्ण):
    return वर्ण in वर्णाः('वल्')


def अस्तेर्भूः_२_४_५२():
    return 'भू'


def ब्रुवो_वचिः_२_४_५३():
    return 'वच्'


def चक्षिङः_ख्याञ्_२_४_५४():
    return 'ख्या'


def अजेर्व्यघञपोः_२_४_५६():
    return 'वी'


def धात्वादेश(पदम्):
    धात्वादेश = {
        'अस्': अस्तेर्भूः_२_४_५२,
        'ब्रू': ब्रुवो_वचिः_२_४_५३,
        'चक्ष्': चक्षिङः_ख्याञ्_२_४_५४,
        'अज्': अजेर्व्यघञपोः_२_४_५६
    }
    धातुः = पदम्.धातुः['धातुः']
    if धातुः in धात्वादेश:
        आदेशः = धात्वादेश[धातुः]()
    else:
        आदेशः = आदेच_उपदेशेऽशिति_६_१_४५(पदम्)
    पदम्.धातुः['आदेशः'] = आदेशः


def आदेच_उपदेशेऽशिति_६_१_४५(पदम्):
    # ' ेैोौ' = ' े'+'ेै'+'ो'+'ौ' - एजन्त
    धातुः = पदम्.धातुः['धातुः']
    if धातुः[-1] in ' ेैोौ' and पदम्.विकरणप्रत्ययः['आर्धधातुकम्']:
        return धातुः[:-1] + 'ा'
    else:
        return धातुः
