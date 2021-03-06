from ashtadhyayi.pratyahara import वर्णाः
from ashtadhyayi.utils import ह्रस्वाः, दीर्घस्वराः, दीर्घाः, दीर्घमात्राश्च, स्वराः, स्वरात्_मात्रा
from ashtadhyayi.sajna import अदेङ्_गुणः_१_१_२


def संहितायाम्_६_१_७२(पूर्वः, अपरः):
    # TODO refactor
    पूर्वः, अपरः = छे_च_६_१_७३(पूर्वः, अपरः)
    पूर्वः, अपरः = इको_यणचि_६_१_७७(पूर्वः, अपरः)
    पूर्वः, अपरः = एचोऽयवायावः_६_१_७८(पूर्वः, अपरः)
    पूर्वः, अपरः = अतो_गुणे_६_१_९७(पूर्वः, अपरः)
    return संयोगः(पूर्वः, अपरः)


def छे_च_६_१_७३(पूर्वः, अपरः):
    हल् = वर्णाः('हल्')
    if पूर्वः[-1] in ह्रस्वाः() or पूर्वः[-1] in हल् or आङ्माङोश्च_६_१_७४(पूर्वः, अपरः) or दीर्घात्_६_१_७५(पूर्वः, अपरः):
        if अपरः[0] == 'छ':
            return पूर्वः + 'त्', अपरः
    return पूर्वः, अपरः


def आङ्माङोश्च_६_१_७४(पूर्वः, अपरः):
    return पूर्वः in ['आङ्', 'माङ्']


def दीर्घात्_६_१_७५(पूर्वः, अपरः):
    हल् = वर्णाः('हल्')
    return पूर्वः[-1] in दीर्घस्वराः() or पूर्वः[-1] in हल्


def पदान्ताद्वा_६_१_७६(पूर्वः, अपरः):
    # TODO
    pass


def इको_यणचि_६_१_७७(पूर्वः, अपरः):
    इक् = दीर्घमात्राश्च(वर्णाः('इक्'))
    यण् = वर्णाः('यण्')
    अच् = वर्णाः('अच्')
    अच् += दीर्घाः(अच्)

    if पूर्वः[-1] in इक् and अपरः[0] in अच्:
        # TODO this index represents यथासङ्ख्यमनुदेशः समानाम् move it as appropriate
        सूची = इक्.index(पूर्वः[-1]) % 4
        पूर्वः = आदेशः(पूर्वः, यण्[सूची])
    return पूर्वः, अपरः


def एचोऽयवायावः_६_१_७८(पूर्वः, अपरः):
    एच् = दीर्घमात्राश्च(वर्णाः('एच्'))
    अच् = वर्णाः('अच्')
    अच् += दीर्घाः(अच्)
    अयवायावः = ['अय्', 'अव्', 'आय्', 'आव्']
    if पूर्वः[-1] in एच् and अपरः[0] in अच्:
        # TODO this index represents यथासङ्ख्यमनुदेशः समानाम् move it as appropriate
        सूची = एच्.index(पूर्वः[-1]) % 4
        पूर्वः = आदेशः(पूर्वः, अयवायावः[सूची])
    return पूर्वः, अपरः


def आदेशः(पूर्वः, अपरः):
    स्थानी = पूर्वः[-1]
    if स्थानी not in स्वराः():
        if अपरः[0] in स्वराः():
            return पूर्वः[:-1] + स्वरात्_मात्रा(अपरः[0]) + अपरः[1:]
        else:
            return पूर्वः[:-1] + '्' + अपरः
    else:
        return पूर्वः[:-1] + अपरः


# TODO rename
def संयोगः(पूर्वः, अपरः):
    स्थानी = पूर्वः[-1]
    if स्थानी == '्' and अपरः[0] in स्वराः():
        return पूर्वः[:-1] + स्वरात्_मात्रा(अपरः[0]) + अपरः[1:]
    return पूर्वः + अपरः


# TODO apadanta
def अतो_गुणे_६_१_९७(पूर्वः, अपरः):
    गुणः = अदेङ्_गुणः_१_१_२()
    if अपरः[0] in गुणः:
        if पूर्वः == 'अ':
            return '', अपरः
        if पूर्वः[-1] in वर्णाः('हल्'):
            return पूर्वः + '्', अपरः
    return पूर्वः, अपरः
