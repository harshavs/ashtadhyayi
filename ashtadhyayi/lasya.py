import sys
import re
from ashtadhyayi.pratyahara import वर्णाः
from ashtadhyayi.it_samjna_prakarana import इत्, उपदेशसंज्ञकः, इत्संज्ञाप्रकरणम्, टित्_वा, ङित्_वा
from ashtadhyayi.aakadaaraat_ekaa_sajna import आनय_तिङ्_प्रत्ययम्
from ashtadhyayi.utils import स्वरात्_मात्रा
from ashtadhyayi.sajna import आनय_टि_संज्ञाम्
from enum import Enum


लकारः = Enum('लकारः', 'लट् लिट् लुट् लृट् लेट् लोट् लङ् लिङ् लुङ् लृङ्')


def तिप्तस्झिसिप्थस्थमिब्वस्मस्_तातांझथासाथांध्वमिड्वहिमहिङ्_३_४_७८():
    return ['तिप्', 'तस्', 'झि', 'सिप्', 'थस्', 'थ', 'मिप्', 'वस्', 'मस्',
            'त', 'आताम्', 'झ', 'थास्', 'आथाम्', 'ध्वम्', 'इड्', 'वहि', 'महिङ्']


# TODO move this to an appropriate place
def आद्यन्तौ_टकितौ_१_१_४६(आगमः, स्थानी):
    इत्_परिणामः = इत्(आगमः, उपदेशसंज्ञकः.आगमः)
    इत्संज्ञकः = इत्_परिणामः['इत्']
    उपदेशः = इत्_परिणामः['उपदेशः']
    if 'ट्' in इत्संज्ञकः:
        आगमः = उपदेशः[:-1] + '्'
        return आगमः + स्थानी
    if 'क्' in इत्संज्ञकः:
        आगमः = उपदेशः[:-1] + '्'
        return स्थानी + आगमः


def टित_आत्मनेपदानां_टेरे_३_४_७९(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    if तिङ्_प्रत्ययः == 'थास्':
        return थासस्से_३_४_८०(तिङन्तरूपम्)
    else:
        टिसंज्ञा = आनय_टि_संज्ञाम्()
        हल् = वर्णाः('हल्')
        टि = re.search(टिसंज्ञा, तिङ्_प्रत्ययः)
        if टि:
            टि = टि.group()
            आदेशः = स्वरात्_मात्रा('ए')
            if टि[0] in हल्:
                आदेशः = टि[0] + आदेशः
            तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace(टि, आदेशः)
        return तिङन्तरूपम्


def थासस्से_३_४_८०(तिङन्तरूपम्):
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = 'से'
    return तिङन्तरूपम्


def लिटस्तझयोरेशिरेच्_३_४_८१(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    if तिङ्_प्रत्ययः == 'त':
        तिङ्_प्रत्ययः = 'एश्'
    elif तिङ्_प्रत्ययः == 'झ':
        तिङ्_प्रत्ययः = 'इरेच्'
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः


def परस्मैपदानां_णलतुसुस्थलथुसणल्वमाः_३_४_८२(पुरुषः, वचनम्):
    return ['णल्', 'अतुस्', 'उस्', 'थल्', 'अथुस्', 'अ', 'णल्', 'व', 'म'][पुरुषः * 3 + वचनम्]


def विदो_लटो_वा_३_४_८३(धातुः, लकारः):
    return धातुः == 'विदँ' and लकारः.लट् == लकारः


def ब्रुवः_पञ्चानामादित_आहो_ब्रुवः_३_४_८४(तिङन्तरूपम्):
    return तिङन्तरूपम्.धातुः == 'ब्रूञ्' and लकारः.लट् == तिङन्तरूपम्.लकारः and तिङन्तरूपम्.पुरुषः * 3 + तिङन्तरूपम्.वचनम् < 5


def लोटो_लङ्वत्_३_४_८५(तिङन्तरूपम्):
    # TODO : find the purpose  ( why like लङ्)
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    if तिङन्तरूपम्.पुरुषः == 2 and स्वरात्_मात्रा('ए') in तिङ्_प्रत्ययः:
        return एत_ऐ_३_४_९३(तिङन्तरूपम्)
    elif 'से' in तिङ्_प्रत्ययः or 'वे' in तिङ्_प्रत्ययः:
        return सवाभ्यां_वामौ_३_४_९१(तिङन्तरूपम्)
    elif स्वरात्_मात्रा('ए') in तिङ्_प्रत्ययः:
        return आमेतः_३_४_९०(तिङन्तरूपम्)
    elif तिङ्_प्रत्ययः == 'मिप्':
        return मेर्निः_३_४_८९(तिङन्तरूपम्)
    elif तिङ्_प्रत्ययः == 'सिप्':
        return सेर्ह्यपिच्च_३_४_८७(तिङन्तरूपम्)
    elif तिङ्_प्रत्ययः == 'अपित्':
        return वा_छन्दसि_३_४_८८(तिङन्तरूपम्)
    else:
        return एरुः_३_४_८६(तिङन्तरूपम्)


def एरुः_३_४_८६(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('इ'), स्वरात्_मात्रा('उ'))
    return तिङन्तरूपम्


def सेर्ह्यपिच्च_३_४_८७(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace('सिप्', 'हि')
    return तिङन्तरूपम्


def वा_छन्दसि_३_४_८८(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace('अपित्', 'हि')
    return तिङन्तरूपम्


def मेर्निः_३_४_८९(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace('मिप्', 'नि')
    return तिङन्तरूपम्


def आमेतः_३_४_९०(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('ए'), 'आम्')
    return तिङन्तरूपम्


def सवाभ्यां_वामौ_३_४_९१(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङ्_प्रत्ययः = re.sub('से.*$', 'स्व', तिङ्_प्रत्ययः)
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = re.sub('वे.*$', 'वम्', तिङ्_प्रत्ययः)
    return तिङन्तरूपम्


def आडुत्तमस्य_पिच्च_३_४_९२(तिङन्तरूपम्):
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = 'आट्'
    return तिङन्तरूपम्


def एत_ऐ_३_४_९३(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('ए'), स्वरात्_मात्रा('ऐ')).replace('ए', 'ऐ')
    return तिङन्तरूपम्


def लेटोऽडाटौ_३_४_९४(तिङन्तरूपम्):
    # TODO - find the purpose
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    if 'स' in तिङ्_प्रत्ययः and तिङन्तरूपम्.पुरुषः == 2:
        return स_उत्तमस्य_३_४_९८(तिङन्तरूपम्)
    elif स्वरात्_मात्रा('इ') in तिङ्_प्रत्ययः and तिङन्तरूपम्.परस्मैपदम्:
        return इतश्च_लोपः_परस्मैपदेषु_३_४_९७(तिङन्तरूपम्)
    elif स्वरात्_मात्रा('ए') in तिङ्_प्रत्ययः:
        return वैतोऽन्यत्र_३_४_९६(तिङन्तरूपम्)
    elif स्वरात्_मात्रा('आ') in तिङ्_प्रत्ययः:
        return आत_ऐ_३_४_९५(तिङन्तरूपम्)


def आत_ऐ_३_४_९५(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('आ'), स्वरात्_मात्रा('ऐ'))
    return तिङन्तरूपम्


def वैतोऽन्यत्र_३_४_९६(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('ए'), स्वरात्_मात्रा('ऐ')).replace('ए', 'ऐ')
    return तिङन्तरूपम्


def इतश्च_लोपः_परस्मैपदेषु_३_४_९७(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('इ'), '')
    return तिङन्तरूपम्


def स_उत्तमस्य_३_४_९८(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace('स्', '').replace('स', '')
    return तिङन्तरूपम्


def नित्यं_ङितः_३_४_९९(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']

    if तिङन्तरूपम्.पुरुषः == 2:
        return स_उत्तमस्य_३_४_९८(तिङन्तरूपम्)

    if तिङ्_प्रत्ययः in ['तस्', 'थस्', 'थ', 'मिप्']:
        return तस्थस्थमिपां_तांतंतामः_३_४_१०१(तिङन्तरूपम्)
    elif स्वरात्_मात्रा('इ') in तिङ्_प्रत्ययः:
        return इतश्च_३_४_१००(तिङन्तरूपम्)


def इतश्च_३_४_१००(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('इ'), '')
    return तिङन्तरूपम्


def तस्थस्थमिपां_तांतंतामः_३_४_१०१(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']

    तस्थस्थमिपां = {
        'तस्': 'ताम्',
        'थस्': 'तम्',
        'थ': 'त',
        'मिप्': 'अमः'
    }
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तस्थस्थमिपां.get(तिङ्_प्रत्ययः)
    return तिङन्तरूपम्


def लिङस्सीयुट्_३_४_१०२(तिङन्तरूपम्):
    प्रत्ययस्य_सूत्रम् = {
       'तिथोः': सुट्_तिथोः_३_४_१०७,
       'इट्': इटोऽत्_३_४_१०६,
       'झ': झस्य_रन्_३_४_१०५,
       'झि': झेर्जुस्_३_४_१०८
    }

    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    प्रत्ययः = 'तिथोः' if 'त' in तिङ्_प्रत्ययः or 'थ' in तिङ्_प्रत्ययः else तिङ्_प्रत्ययः
    सूत्रम् = प्रत्ययस्य_सूत्रम्.get(प्रत्ययः)

    if सूत्रम्:
        सूत्रम्(तिङन्तरूपम्)

    if तिङन्तरूपम्.परस्मैपदम्:
        return यासुट्_परस्मैपदेषूदात्तो_ङिच्च_३_४_१०३(तिङन्तरूपम्)
    else:
        return आद्यन्तौ_टकितौ_१_१_४६('सीयुट्', तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'])


def यासुट्_परस्मैपदेषूदात्तो_ङिच्च_३_४_१०३(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = आद्यन्तौ_टकितौ_१_१_४६('यासुट्', तिङ्_प्रत्ययः)
    return तिङन्तरूपम्


# TODO : find the purpose of this
def किदाशिषि_३_४_१०४():
    return ''


def झस्य_रन्_३_४_१०५(तिङन्तरूपम्):
    return तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'].replace('झ', 'रन्')


def इटोऽत्_३_४_१०६(तिङन्तरूपम्):
    return तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'].replace('इट्', 'अत्')


def सुट्_तिथोः_३_४_१०७(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः']
    तिथोः = 'त' if 'त' in तिङ्_प्रत्ययः else 'थ'
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः.replace(तिथोः, आद्यन्तौ_टकितौ_१_१_४६('सुट्', तिथोः))
    return तिङन्तरूपम्


def झेर्जुस्_३_४_१०८(तिङन्तरूपम्):
    if सिजभ्यस्तविदिभ्यः_च_३_४_१०९(तिङन्तरूपम्.तिङ्_प्रत्ययः):
        return तिङन्तरूपम्.तिङ्_प्रत्ययः.replace('झि', इत्संज्ञाप्रकरणम्('जुस्', उपदेशसंज्ञकः.प्रत्ययः))
    return तिङन्तरूपम्


def सिजभ्यस्तविदिभ्यः_च_३_४_१०९(तिङन्तरूपम्):
    return (तिङन्तरूपम्.विकरणप्रत्ययः.प्रत्ययः == 'सिच्' or तिङन्तरूपम्.विकरणप्रत्ययः.संज्ञा in ['अभ्यस्तम्', 'द्वित्वम्']
            or तिङन्तरूपम्.धातुः == 'विद्')


def आतः_३_४_११०(तिङन्तरूपम्):
    विकरणप्रत्ययः = तिङन्तरूपम्.विकरणप्रत्ययः
    return (विकरणप्रत्ययः.प्रत्ययः == 'सिच्' and विकरणप्रत्ययः.परिणामः is None
            and विकरणप्रत्ययः.अङ्गम्[:-1] in ['आ', स्वरात्_मात्रा('आ')])


def लङः_शाकटायनस्यैव_३_४_१११(तिङन्तरूपम्):
    # TODO : purpose of this sutra?
    return तिङन्तरूपम्


def द्विषश्च_३_४_११२(तिङन्तरूपम्):
    # TODO : same as above
    return तिङन्तरूपम्


def लस्य_३_४_७७(तिङन्तरूपम्):
    तिङ्_प्रत्ययाः = तिप्तस्झिसिप्थस्थमिब्वस्मस्_तातांझथासाथांध्वमिड्वहिमहिङ्_३_४_७८()
    तिङ्_प्रत्ययः = आनय_तिङ्_प्रत्ययम्(तिङन्तरूपम्.परस्मैपदम्, तिङन्तरूपम्.पुरुषः, तिङन्तरूपम्.वचनम्, तिङ्_प्रत्ययाः)
    तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = तिङ्_प्रत्ययः
    पुरुषः = तिङन्तरूपम्.पुरुषः
    वचनम् = तिङन्तरूपम्.वचनम्

    if टित्_वा(तिङन्तरूपम्.लकारः.name) and not तिङन्तरूपम्.परस्मैपदम्:
        if तिङन्तरूपम्.लकारः == लकारः.लिट् and तिङ्_प्रत्ययः in ['त', 'झ']:
            लिटस्तझयोरेशिरेच्_३_४_८१(तिङन्तरूपम्)
        else:
            टित_आत्मनेपदानां_टेरे_३_४_७९(तिङन्तरूपम्)

    if तिङन्तरूपम्.परस्मैपदम्:
        if तिङन्तरूपम्.लकारः == लकारः.लिट्:
            तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = परस्मैपदानां_णलतुसुस्थलथुसणल्वमाः_३_४_८२(पुरुषः, वचनम्)

        ब्रुवः_पञ्चानामादि = ब्रुवः_पञ्चानामादित_आहो_ब्रुवः_३_४_८४(तिङन्तरूपम्)
        if विदो_लटो_वा_३_४_८३(तिङन्तरूपम्.धातुः, तिङन्तरूपम्.लकारः) or ब्रुवः_पञ्चानामादि:
            तिङन्तरूपम्.तिङ्_प्रत्ययः['प्रत्ययः'] = [तिङ्_प्रत्ययः, परस्मैपदानां_णलतुसुस्थलथुसणल्वमाः_३_४_८२(पुरुषः, वचनम्)]
        if ब्रुवः_पञ्चानामादि:
            # TODO : return this as well
            तिङन्तरूपम्.धातुः = [तिङन्तरूपम्.धातुः, 'आह्']

    if ङित्_वा(तिङन्तरूपम्.लकारः.name):
        नित्यं_ङितः_३_४_९९(तिङन्तरूपम्)

    लकार_सूत्राणि = {
        लकारः.लोट्: लोटो_लङ्वत्_३_४_८५,
        लकारः.लेट्: लेटोऽडाटौ_३_४_९४,
        लकारः.लिङ्: लिङस्सीयुट्_३_४_१०२
    }

    if लकार_सूत्राणि.get(तिङन्तरूपम्.लकारः) is not None:
        लकार_सूत्राणि.get(तिङन्तरूपम्.लकारः)(तिङन्तरूपम्)

    return तिङन्तरूपम्


if __name__ == '__main__':
    print(लस्य_३_४_७७(sys.argv[1], sys.argv[2], sys.argv[3] == 'परस्मैपदम्', int(sys.argv[4]), int(sys.argv[5])))
