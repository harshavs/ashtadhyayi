from ashtadhyayi.dhaatoho import सार्वधातुकम्_आर्धधातुकम्, धातोरेकाचो_हलादेः_क्रियासमभिहारे_यङ्_३_१_२२
from ashtadhyayi.dhaatoho import सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो_णिच्_३_१_२५
from ashtadhyayi.angasya import आर्धधातुकस्येड्_वलादेः_७_२_३५, मिदेर्गुणः_७_३_८२, झोऽन्तः_७_१_३
from ashtadhyayi.angasya import सार्वधातुकार्धधातुकयोः_७_३_८४, इदितो_नुम्_धातोः_७_१_५८, अतो_दीर्घो_यञि_७_३_१०१
from ashtadhyayi.lasya import लस्य_३_४_७७, लकारः
from ashtadhyayi.aardhadhatuke import आर्धधातुके_२_४_३५
from ashtadhyayi.upadeshe import आदेच_उपदेशेऽशिति_६_१_४५, धात्वादेः_षः_सः_६_१_६४
from ashtadhyayi.it_samjna_prakarana import उपदेशसंज्ञकः, इत्
from ashtadhyayi.sajna import मिदचोऽन्त्यात्परः_१_१_४७, अनुदात्तङित_आत्मनेपदम्_१_३_१२
from ashtadhyayi.purvatraasiddham import उपधायां_च_८_२_७८, नश्चापदान्तस्य_झलि_८_३_२४, ससजुषो_रुः_८_२_६६
from ashtadhyayi.samhitaayaam import संहितायाम्_६_१_७२


class तिङन्तरूपम्:

    def __init__(self, धातुः, लकारः, परस्मैपदम्, पुरुषः, वचनम्):
        self.धातुः = धातुः
        self.लकारः = लकारः
        self.परस्मैपदम् = परस्मैपदम्
        self.पुरुषः = पुरुषः
        self.वचनम् = वचनम्
        self.तिङ्_प्रत्ययः = {'प्रत्ययः': None, 'सार्वधातुकम्': False, 'आर्धधातुकम्': False}
        self.विकरणप्रत्ययः = {'प्रत्ययः': None, 'सार्वधातुकम्': False, 'आर्धधातुकम्': False}
        self.कृत्प्रत्ययः = {'प्रत्ययः': None, 'सार्वधातुकम्': False, 'आर्धधातुकम्': False}
        self.लकारार्थः = None
        self.तिङन्तरूपम् = ''

    def __str__(self):
        return self.तिङन्तरूपम्


def तिङन्तम्(धातुः, लकारः, परस्मैपदम्, पुरुषः, वचनम्):
    पदम् = तिङन्तरूपम्(धातुः, लकारः, परस्मैपदम्, पुरुषः, वचनम्)

    # इत्
    इत्_परिणामः = इत्(पदम्.धातुः['उपदेशः'], उपदेशसंज्ञकः.धातुः)
    पदम्.धातुः['धातुः'] = इत्_परिणामः['उपदेशः']
    पदम्.धातुः['इत्'] = इत्_परिणामः['इत्']
    if not पदम्.धातुः['धातुः']:
        पदम्.धातुः['धातुः'] = पदम्.धातुः['उपदेशः']

    # सत्वविधिः + सत्वविधिः
    धात्वादेः_षः_सः_६_१_६४(पदम्)

    # नुमागमविधिः
    इदितो_नुम्_धातोः_७_१_५८(पदम्)
    if पदम्.धातुः.get('आगमः'):
        इत्_परिणामः = इत्(पदम्.धातुः['आगमः'], उपदेशसंज्ञकः.आगमः)
        परिणामः = मिदचोऽन्त्यात्परः_१_१_४७(इत्_परिणामः['इत्'], इत्_परिणामः['उपदेशः'], पदम्.धातुः['धातुः'])
        if परिणामः:
            पदम्.धातुः['धातुः'] = परिणामः + नश्चापदान्तस्य_झलि_८_३_२४(परिणामः[1], परिणामः[2])
        else:
            पदम्.धातुः['धातुः'] += इत्_परिणामः['उपदेशः']

    # उपधादीर्घविधिः
    उपधायां_च_८_२_७८(पदम्)

    # प्रक्रिया
    धातोरेकाचो_हलादेः_क्रियासमभिहारे_यङ्_३_१_२२(पदम्)
    लस्य_३_४_७७(पदम्)
    सार्वधातुकम्_आर्धधातुकम्(पदम्)
    इडागमविधिः(पदम्)
    धात्वादेशः(पदम्)
    अतिदेशः_अङ्गकार्यः(पदम्)
    सामान्यअङ्गकार्यः(पदम्)
    षत्वविधिः(पदम्)
    सन्धि(पदम्)

    return पदम्


def इडागमविधिः(पदम्):
    आर्धधातुकस्येड्_वलादेः_७_२_३५(पदम्)


def धात्वादेशः(पदम्):
    आर्धधातुके_२_४_३५(पदम्)
    आदेशः = आदेच_उपदेशेऽशिति_६_१_४५(पदम्)
    if आदेशः:
        पदम्.धातुः['आदेशः'] = आदेशः


def अतिदेशः_अङ्गकार्यः(पदम्):
    return मिदेर्गुणः_७_३_८२(पदम्)


def सामान्यअङ्गकार्यः(पदम्):
    return सार्वधातुकार्धधातुकयोः_७_३_८४(पदम्)


def षत्वविधिः(पदम्):
    return None


def तिङ्_प्रत्ययाः(रूपम्):
    return [[तिङ्_प्रत्ययः(रूपम्, पुरुषः, वचनम्) for वचनम् in range(3)] for पुरुषः in range(3)]


def तिङ्_प्रत्ययः(रूपम्, पुरुषः, वचनम्):
    return लस्य_३_४_७७(तिङन्तरूपम्(*रूपम्, पुरुषः, वचनम्)).तिङ्_प्रत्ययः['प्रत्ययः']


def सन्धि(पदम्):
    रू = ''

    धातुः = पदम्.धातुः
    आदेशः = धातुः.get('आदेशः')
    if आदेशः:
        रू = इत्(आदेशः, उपदेशसंज्ञकः.आदेशः)['उपदेशः']
    else:
        रू = इत्(धातुः.get('धातुः'), उपदेशसंज्ञकः.धातुः)['उपदेशः']

    आगमः = धातुः.get('आगमः')
    if आगमः:
        रू = संहितायाम्_६_१_७२(रू, इत्(आगमः, उपदेशसंज्ञकः.आगमः)['उपदेशः'])

    विकरणप्रत्ययः = पदम्.विकरणप्रत्ययः
    इडागमः = विकरणप्रत्ययः.get('इडागमः')
    if इडागमः:
        रू = संहितायाम्_६_१_७२(रू, 'इ')

    if विकरणप्रत्ययः['प्रत्ययः']:
        रू = संहितायाम्_६_१_७२(रू, इत्(विकरणप्रत्ययः['प्रत्ययः'], उपदेशसंज्ञकः.प्रत्ययः)['उपदेशः'])

    if पदम्.तिङ्_प्रत्ययः['प्रत्ययः']:
        झोऽन्तः_७_१_३(पदम्)
        रू = अतो_दीर्घो_यञि_७_३_१०१(रू, पदम्.तिङ्_प्रत्ययः['प्रत्ययः'])
        रू = संहितायाम्_६_१_७२(रू, इत्(पदम्.तिङ्_प्रत्ययः['प्रत्ययः'], उपदेशसंज्ञकः.प्रत्ययः, True)['उपदेशः'])

    रू = ससजुषो_रुः_८_२_६६(रू)

    पदम्.तिङन्तरूपम् = रू


def धातुरूपम्(उपदेशः, गणः):
    धातुः = {'उपदेशः': उपदेशः, 'गणः': गणः}
    धातुः['इत्'] = इत्(उपदेशः, उपदेशसंज्ञकः.धातुः)
    णिच् = सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो_णिच्_३_१_२५(गणः)
    धातुः['पदम्'] = अनुदात्तङित_आत्मनेपदम्_१_३_१२(धातुः['इत्'], णिच्)

    if धातुः['पदम्'] == 'उ.प':
        परस्मैपदम् = [True, False]
    elif धातुः['पदम्'] == 'आ.प':
        परस्मैपदम् = [False]
    else:
        परस्मैपदम् = [True]

    पुरुषाः = ['प्रथमपुरुषः', 'मध्यमपुरुषः', 'उत्तमपुरुषः']
    वचनाः = ['एकवचनम्', 'द्विवचनम्', 'बहुवचनम्']

    परिणामाः = {}
    for पदम् in परस्मैपदम्:
        परिणामाः[पदम्] = {}
        पदपरिणामाः = परिणामाः[पदम्]
        for ल in लकारः:
            पदपरिणामाः[str(ल)] = {}
            लकारपरिणामाः = पदपरिणामाः[str(ल)]
            for पुरुषः in range(0, 3):
                पु = पुरुषाः[पुरुषः]
                लकारपरिणामाः[पु] = {}
                पुरुषपरिणामाः = लकारपरिणामाः[पु]
                for वचनम् in range(0, 3):
                    व = वचनाः[वचनम्]
                    पुरुषपरिणामाः[व] = str(तिङन्तम्(धातुः, ल, पदम्, पुरुषः, वचनम्))
    return परिणामाः
