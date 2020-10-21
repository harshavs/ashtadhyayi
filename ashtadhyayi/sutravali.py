from os import listdir
import ast
import _ast
import re

GIT = 'https://github.com/harshavs/ashtadhyayi/blob/master/'
SANKHYAAHA = '१२३४५६७८९०'
NUMERALS = '1234567890'


def getNumber(sankhya):
    return int(''.join([NUMERALS[SANKHYAAHA.index(s)] for s in sankhya]))


def सूत्रावली():
    path = 'ashtadhyayi/'
    sutras = []
    for f in listdir(path):
        if f.endswith(".py"):
            with open(path+f) as prakarana:
                vruksha = ast.parse(prakarana.read())
                for shaka in vruksha.body:
                    if isinstance(shaka, _ast.FunctionDef):
                        sutra = shaka.name
                        sutra_sankhya = re.search('^(.+)_([१२३४५६७८९०]+)_([१२३४५६७८९०]+)_([१२३४५६७८९०]+)', sutra)
                        if sutra_sankhya:
                            sutras.append({
                                'sutra': sutra_sankhya.group(1),
                                'adhyayayaha': sutra_sankhya.group(2),
                                'pada': sutra_sankhya.group(3),
                                'sankhya': sutra_sankhya.group(4),
                                'file': path + f,
                                'line': shaka.lineno
                            })
    sutras = sorted(sutras, key=lambda k: (k['adhyayayaha'], k['pada'], getNumber(k['sankhya'])))
    list = '<ul>'
    adhyayayaha = ''
    pada = ''
    for sutra in sutras:
        if adhyayayaha != sutra['adhyayayaha']:
            list += '' if adhyayayaha == '' else '</ul></li></ul></li>'
            adhyayayaha = sutra['adhyayayaha']
            pada = sutra['pada']
            list += '<li><h1>अध्यायः - {adhyayayaha}</h1><ul><li><h2>पादः - {pada}</h2><ul>'.format(
                adhyayayaha=adhyayayaha,
                pada=pada)
        elif pada != sutra['pada']:
            pada = sutra['pada']
            list += '</ul></li><li><h2>पादः - {pada}</h2><ul>'.format(pada=pada)
        list += '<li><a href="{git}{path}#L{line}">{sankhya} - {sutra}</a></li>'.format(
            git=GIT,
            path=sutra['file'],
            line=sutra['line'],
            sankhya=sutra['sankhya'],
            sutra=sutra['sutra'])
    list += '</ul></li></ul></li></ul>'
    list += '<br/><div> Count - {count}'.format(count=len(sutras))

    open('docs/sutravali.html', 'w+').write(list)


सूत्रावली()
