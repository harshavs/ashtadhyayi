from ashtadhyayi.it_samjna_prakarana import ङित्_वा, कित्_वा
from ashtadhyayi.sajna import अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५
from ashtadhyayi.utils import हलन्तः, अनुनासिकान्तः, अनुदात्त


def असिद्धवदत्राभात्_६_४_२२(पदम्):
    return None


def श्नान्नलोपः_६_४_२३(पदम्):
    विकरणप्रत्ययः = पदम्.विकरणप्रत्ययः['प्रत्ययः']
    तिङ्_प्रत्ययः = पदम्.तिङ्_प्रत्ययः['प्रत्ययः']
    कृत्प्रत्ययः = पदम्.कृत्प्रत्ययः['प्रत्ययः']
    if विकरणप्रत्ययः == 'श्नम्' and (तिङ्_प्रत्ययः[0] == 'न' or कृत्प्रत्ययः[0] == 'न'):
        return {'आश्रयौ': ['श्नम्', 'न'], 'कार्यम्': lambda पदम्: लोपः(पदम्, 1, False)}


def लोपः(पदम्, अक्षराणि, विकरणप्रत्ययः=True):
    if विकरणप्रत्ययः:
        पदम्.विकरणप्रत्ययः['प्रत्ययः'] = पदम्.विकरणप्रत्ययः['प्रत्ययः'][अक्षराणि:]
    else:
        if पदम्.तिङ्_प्रत्ययः['प्रत्ययः']:
            पदम्.तिङ्_प्रत्ययः['प्रत्ययः'] = पदम्.तिङ्_प्रत्ययः['प्रत्ययः'][अक्षराणि:]
        else:
            पदम्.कृत्प्रत्ययः['प्रत्ययः'] = पदम्.कृत्प्रत्ययः['प्रत्ययः'][अक्षराणि:]


def अनिदितां_हल_उपधायाः_क्ङिति_६_४_२४(पदम्):
    if 'ि' not in पदम्.धातुः['इत्'] and 'इ' not in पदम्.धातुः['इत्']:
        धातुः = पदम्.धातुः['धातुः']
        उपधा = अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५(धातुः)
        if हलन्तः(धातुः) and उपधा == 'न्':
            if पदम्.विकरणप्रत्ययः['प्रत्ययः']:
                प्रत्ययः = पदम्.विकरणप्रत्ययः['प्रत्ययः']
            elif पदम्.कृत्प्रत्ययः['प्रत्ययः']:
                प्रत्ययः = पदम्.कृत्प्रत्ययः['प्रत्ययः']
            else:
                प्रत्ययः = पदम्.तिङ्_प्रत्ययः['प्रत्ययः']
            कित् = कित्_वा(प्रत्ययः)
            if कित् or ङित्_वा(प्रत्ययः):
                # TODO lopa
                return {'आश्रयौ': ['क्' if कित् else 'ङ्', 'न्'], 'कार्यम्': lambda पदम्: पदम्.धातुः.replace(उपधा, '')}


def दंशसञ्जस्वञ्जां_शपि_६_४_२५(पदम्):
    धातुः = पदम्.धातुः['धातुः']
    रञ्जेश्च = रञ्जेश्च_६_४_२६(पदम्)
    if धातुः in ['दंश्', 'सञ्ज्', 'स्वञ्ज्'] or रञ्जेश्च:
        उपधा = अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५(धातुः)
        if उपधा == 'न्':
            घञि = घञि_च_भावकरणयोः_६_४_२७(पदम्)
            if पदम्.विकरणप्रत्ययः['प्रत्ययः'] == 'शप्' or (रञ्जेश्च and घञि):
                return {'आश्रयौ': ['घञ्' if घञि else 'शप्', 'न्'], 'कार्यम्': lambda पदम्: पदम्.धातुः.replace(उपधा, '')}


def रञ्जेश्च_६_४_२६(पदम्):
    return पदम्.धातुः['धातुः'] == 'रञ्ज्'


def घञि_च_भावकरणयोः_६_४_२७(पदम्):
    # TODO bhavakarmanayoho
    return पदम्.विकरणप्रत्ययः['प्रत्ययः'] == 'घञ्' and नाञ्चेः_पूजायाम्_६_४_३०(पदम्)


def स्यदो_जवे_६_४_२८(पदम्):
    # TODO
    return None


def अवोदैधौद्मप्रश्रथहिमश्रथाः_६_४_२९(पदम्):
    # TODO
    return None


def नाञ्चेः_पूजायाम्_६_४_३०(पदम्):
    return not (पदम्.धातुः['धातुः'] == 'अञ्च्' and पदम्.धातुः['लकारार्थः'] in ['पूजायाम्'])


def क्त्वि_स्कन्दिस्यन्दोः_६_४_३१(पदम्):
    return not (पदम्.धातुः['धातुः'] in ['स्कन्द्', 'स्यन्द्'] and पदम्.कृत्प्रत्ययः['प्रत्ययः'] == 'क्त्वा')


def जान्तनशां_विभाषा_६_४_३२(पदम्):
    if पदम्.धातुः['धातुः'][-2:] == 'ज्' or पदम्.धातुः['धातुः'] == 'नश्':
        if पदम्.कृत्प्रत्ययः['प्रत्ययः'] == 'क्त्वा':
            return [True, False]
    return False


def भञ्जेश्च_चिणि_६_४_३३(पदम्):
    if पदम्.धातुः['धातुः'] == 'भञ्ज्':
        if पदम्.कृत्प्रत्ययः['प्रत्ययः'] == 'चिण्':
            return [True, False]
    return False


def शास_इदङ्हलोः_६_४_३४(पदम्):
    if पदम्.धातुः['धातुः'] == 'शास्':
        # उपधा = अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५(धातुः)
        # TODO
        return None


def शा_हौ_६_४_३५(पदम्):
    if पदम्.धातुः['धातुः'] == 'शास्':
        if पदम्.विकरणप्रत्ययः['प्रत्ययः'] == 'हि':
            # 'शा' - aadesha
            return None


def हन्तेर्जः_६_४_३६(पदम्):
    if पदम्.धातुः['धातुः'] == 'हन्':
        # ja aadesha
        return None


def अनुदात्तोपदेशवनतितनोत्यादीनामनुनासिक_लोपो_झलि_क्ङिति_६_४_३७(पदम्):
    if अनुनासिकान्तः(पदम्.धातुः['धातुः']) and अनुदात्त in पदम्.धातुः['उपदेशः']:
        # jhaladi?
        return None


def वा_ल्यपि_६_४_३८(पदम्):
    if पदम्.कृत्प्रत्ययः['प्रत्ययः'] == 'ल्यप्':
        return None


def न_क्तिचि_दीर्घश्च_६_४_३९(पदम्):
    if पदम्.कृत्प्रत्ययः['प्रत्ययः'] == 'ल्यप्':
        return False


def गमः_क्वौ_६_४_४०(पदम्):
    return None
