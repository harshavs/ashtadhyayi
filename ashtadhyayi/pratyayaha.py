import re
from ashtadhyayi.pratyahara import वर्णाः
from ashtadhyayi.aakadaaraat_ekaa_sajna import गुरुमत्
from ashtadhyayi.sajna import अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५
from ashtadhyayi.utils import स्वरात्_मात्रा


def प्रत्ययः_३_१_१(प्रत्ययः):
    परश्च_३_१_२(प्रत्ययः)


def परश्च_३_१_२(प्रत्ययः):
    if प्रत्ययः.संज्ञा in ['सुप्', 'पित्']:
        अनुदात्तौ_सुप्पितौ_३_१_४(प्रत्ययः)
    else:
        आद्युदात्तश्च_३_१_३(प्रत्ययः)


def आद्युदात्तश्च_३_१_३(प्रत्ययः):
    # TODO :
    return


def अनुदात्तौ_सुप्पितौ_३_१_४(प्रत्ययः):
    # TODO :
    return


def गुप्तिज्किद्भ्यः_सन्_३_१_५(पदम्):
    if पदम्.धातुः in ['गुप्', 'तिज्', 'कित्']:
        पदम्.प्रत्ययः.संज्ञा = 'सन्'


def मान्बधदान्शान्भ्यो_दीर्घश्चाभ्यासस्य_३_१_६(पदम्):
    if पदम्.धातुः in ['मान्', 'बध', 'दान्', 'शान्']:
        पदम्.प्रत्ययः.संज्ञा = 'सन्'
        # TODO पदम्.अभ्यासः deergha


def धातोः_कर्मणः_समानकर्तृकादिच्छायां_वा_३_१_७(पदम्):
    # TODO :
    pass


def सुप_आत्मनः_क्यच्_३_१_८():
    # TODO :
    pass


def काम्यच्च_३_१_९():
    # TODO :
    pass


def उपमानादाचारे_३_१_१०():
    # TODO :
    pass


def कर्तुः_क्यङ्_सलोपश्च_३_१_११():
    # TODO :
    pass


def भृशादिभ्यो_भुव्यच्वेर्लोपश्च_हलः_३_१_१२():
    # TODO :
    pass


def लोहितादिडाज्भ्यः_क्यष्_३_१_१३():
    # TODO
    pass


def कष्टाय_क्रमणे_३_१_१४():
    # TODO
    pass


def कर्मणः_रोमन्थतपोभ्यां_वर्तिचरोः_३_१_१५():
    # TODO
    pass


def बाष्पोष्मभ्यामुद्वमने_३_१_१६():
    # TODO
    pass


def शब्दवैरकलहाभ्रकण्वमेघेभ्यः_करणे_३_१_१७():
    # TODO
    pass


def सुखादिभ्यः_कर्तृवेदनायाम्_३_१_१८():
    # TODO
    pass


def नमोवरिवश्चित्रङः_क्यच्_३_१_१९():
    # TODO
    pass


def पुच्छभाण्डचीवराण्णिङ्_३_१_२०():
    # TODO
    pass


def मुण्डमिश्रश्लक्ष्णलवणव्रतवस्त्रहलकलकृततूस्तेभ्यो_णिच्_३_१_२१():
    # TODO
    pass


def धातोरेकाचो_हलादेः_क्रियासमभिहारे_यङ्_३_१_२२(पदम्):

    if पदम्.लकारः == 'लेट्':
        सिब्बहुलं_लेटि_३_१_३४(पदम्)

    if पदम्.धातुः == 'कमेर्':
        आयादयः = कमेर्णिङ्_३_१_३०()

    if पदम्.धातुः == 'ऋति':
        आयादयः = ऋतेरीयङ्_३_१_२९()

    if पदम्.धातुः in 'गुपू-धूप-विच्छि-पणि-पनि':
        आयादयः = गुपूधूपविच्छिपणिपनिभ्य_आयः_३_१_२८()

    if पदम्.आर्धधातुकम्:
        पदम्.प्रत्ययः = आयादय_आर्धधातुके_वा_३_१_३१(आयादयः)
    else:
        पदम्.प्रत्ययः = आयादयः

    # TODO
    pass


def नित्यं_कौटिल्ये_गतौ_३_१_२३():
    # TODO
    pass


def लुपसदचरजपजभदहदशगॄभ्यो_भावगर्हायाम्_३_१_२४():
    # TODO
    pass


def सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो_णिच्_३_१_२५():
    # TODO
    pass


def हेतुमति_च_३_१_२६():
    # TODO
    pass


def कण्ड्वादिभ्यो_यक्_३_१_२७():
    # TODO
    pass


def गुपूधूपविच्छिपणिपनिभ्य_आयः_३_१_२८():
    return 'आय'


def ऋतेरीयङ्_३_१_२९():
    return 'ईयङ्'


def कमेर्णिङ्_३_१_३०():
    return 'णिङ्'


def आयादय_आर्धधातुके_वा_३_१_३१(आयादयः):
    if आयादयः:
        return [None, आयादयः]


def सनाद्यन्ता_धातवः_३_१_३२():
    # TODO
    pass


def स्यतासी_लृलुटोः_३_१_३३(पदम्):
    if पदम्.लकारः in ['लृङ्', 'लृट्']:
        पदम्.प्रत्ययः = 'स्य'
    if पदम्.लकारः == 'लुट्':
        पदम्.प्रत्ययः = 'तास्'
    return


def सिब्बहुलं_लेटि_३_१_३४(पदम्):
    पदम्.प्रत्ययः = 'सिप्'


def कास्प्रत्ययादाममन्त्रे_लिटि_३_१_३५(पदम्):
    if पदम्.लकारः == 'लिट्':
        if पदम्.धातुः == 'कास्' or इजादेश्च_गुरुमतोऽनृच्छः_३_१_३६(पदम्) or दयायासश्च_३_१_३७(पदम्):
            पदम्.प्रत्ययः = 'आम्'

        if उषविदजागृभ्योऽन्यतरस्याम्_३_१_३८(पदम्) or भीह्रीभृहुवां_श्लुवच्च_३_१_३९(पदम्):
            पदम्.प्रत्ययः = [None, 'आम्']


def इजादेश्च_गुरुमतोऽनृच्छः_३_१_३६(पदम्):
    if पदम्.धातुः != 'ऋच्छ्':
        इच् = वर्णाः('इच्')
        # TODO use savarnas,
        इजादिः = '^[{इच्}ईऊॠ].'.format(इच्=इच्)
        if re.search(इजादिः, पदम्.धातुः) and गुरुमत्(पदम्.धातुः):
            return True
    return False


def दयायासश्च_३_१_३७(पदम्):
    return पदम्.धातुः in ['दय', 'अय', 'आस']


def उषविदजागृभ्योऽन्यतरस्याम्_३_१_३८(पदम्):
    return पदम्.धातुः in ['उष', 'विद', 'जगृ']


def भीह्रीभृहुवां_श्लुवच्च_३_१_३९(पदम्):
    # TODO श्लुवच्च
    return पदम्.धातुः in ['भी', 'ह्री', 'भृ', 'हु']


def कृञ्_चानुप्रयुज्यते_लिटि_३_१_४०(पदम्):
    # TODO चानुप्रयुज्यते
    return पदम्.धातुः in ['कृ', 'भू', 'अस्']


def विदाङ्कुर्वन्त्वित्यन्यतरस्याम्_३_१_४१(पदम्):
    # TODO अन्यतरस्याम्
    return पदम्.धातुः == 'विद्'


def अभ्युत्सादयांप्रजनयांचिकयांरमयामकः_पावयांक्रियाद्विदामक्रन्निति_च्छन्दसि_३_१_४२():
    # TODO
    return


def च्लि_लुङि_३_१_४३(पदम्):
    if पदम्.लकारः == 'लुङ्':
        पदम्.प्रत्ययः = 'च्लि'


def च्लेः_सिच्_३_१_४४(पदम्):
    if पदम्.प्रत्ययः == 'च्लि':
        पदम्.प्रत्ययः = 'सिच्'


def शल_इगुपधादनिटः_क्सः_३_१_४५(पदम्):
    इक् = वर्णाः('इक्')
    इक् += स्वरात्_मात्रा(इक्)
    शल् = वर्णाः('शल्')
    # TODO अनिट्
    if पदम्.प्रत्ययः == 'च्लि' and अलोऽन्त्यात्_पूर्व_उपधा_१_१_६५(पदम्.धातुः) in इक् and पदम्.धातुः[-2] in शल्:
        पदम्.प्रत्ययः = 'क्स'


def श्लिष_आलिङ्गने_३_१_४६(पदम्):
    if पदम्.धातुः == 'श्लिष्' and पदम्.धातुः.अर्थः == 'आलिङ्गने':
        पदम्.प्रत्ययः = 'क्स'


def न_दृशः_३_१_४७(पदम्):
    return पदम्.धातुः == 'दृश्'


def णिश्रिद्रुस्रुभ्यः_कर्तरि_चङ्_३_१_४८(पदम्):
    if पदम्.धातुः.अतिदेशः == 'णिङ्' or पदम्.धातुः in ['श्रि', 'द्रु', 'स्रु']:
        if पदम्.प्रत्ययः == 'च्लि' and पदम्.प्रयोगः == 'कर्तरि':
            पदम्.प्रत्ययः = 'चङ्'


def विभाषा_धेट्श्व्योः_३_१_४९(पदम्):
    if पदम्.धातुः in ['धेट्', 'श्वि']:
        पदम्.प्रत्ययः = [पदम्.प्रत्ययः, 'चङ्']


def गुपेश्छन्दसि_३_१_५०(पदम्):
    # TODO छन्दसि
    if पदम्.धातुः == 'गुप्' and not नोनयतिध्वनयत्येलयत्यर्दयतिभ्यः_३_१_५१(पदम्):
        पदम्.प्रत्ययः = [पदम्.प्रत्ययः, 'चङ्']


def नोनयतिध्वनयत्येलयत्यर्दयतिभ्यः_३_१_५१(पदम्):
    return पदम्.धातुः in ['ऊन', 'ध्वन', 'इल', 'अर्द']


def अस्यतिवक्तिख्यातिभ्योऽङ्_३_१_५२(पदम्):
    if पदम्.धातुः in ['असुँ', 'वच्', 'ख्या']:
        पदम्.प्रत्ययः = 'अङ्'


def लिपिसिचिह्वश्च_३_१_५३(पदम्):
    if पदम्.धातुः in ['लिप्', 'सिच्', 'ह्वे']:
        if आत्मनेपदेष्वन्यतरस्याम्_३_१_५४():
            पदम्.प्रत्ययः = [पदम्.प्रत्ययः, 'अङ्']
        else:
            पदम्.प्रत्ययः = 'अङ्'


def आत्मनेपदेष्वन्यतरस्याम्_३_१_५४(पदम्):
    return not पदम्.परस्मैपदम्


def पुषादिद्युताद्यॢदितः_परस्मैपदेषु_३_१_५५(पदम्):
    # TODO do ऌदित
    if पदम्.गणः in ['पुषादि', 'द्युतादि'] and पदम्.परस्मैपदम्:
        पदम्.प्रत्ययः = 'अङ्'
