from ashtadhyayi.utils import स्वरमात्राः, स्वराः
import re


def एकाचो_द्वे_प्रथमस्य_६_१_१(पदम्):
    द्वितीयम् = अजादेर्द्वितीयस्य_६_१_२(पदम्)
    if not द्वितीयम्:
        द्वितीयम् = पदम्.धातुः['धातुः']
    पूर्वोऽभ्यासः_६_१_४(पदम्, पदम्.धातुः['धातुः'])
    उभे_अभ्यस्तम्_६_१_५(पदम्, द्वितीयम्)


def अजादेर्द्वितीयस्य_६_१_२(पदम्):
    अजादिप्रतिरूपम् = '^([{स्वराः}])(.*[{स्वरमात्राः}].*)$'.format(स्वराः=स्वराः(), स्वरमात्राः=स्वरमात्राः())
    अजादिः = re.search(अजादिप्रतिरूपम्, पदम्.धातुः['धातुः'])
    if अजादिः:
        द्वितीयम् = अजादिः.group(2)
        if न_न्द्राः_संयोगादयः_६_१_३(द्वितीयम्):
            # leave first two chars, one for halanta
            return द्वितीयम्[2:]
        return द्वितीयम्


def न_न्द्राः_संयोगादयः_६_१_३(द्वितीयम्):
    return द्वितीयम्[0] in ['न', 'द', 'र']


def पूर्वोऽभ्यासः_६_१_४(पदम्, अभ्यासः):
    पदम्.धातुः['अभ्यासः'] = अभ्यासः


def उभे_अभ्यस्तम्_६_१_५(पदम्, द्वितीयम्):
    पदम्.धातुः['अभ्यस्तम्'] = {'प्रथमम्': पदम्.धातुः['अभ्यासः'], 'द्वितीयम्': द्वितीयम्}
