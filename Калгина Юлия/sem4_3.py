import xml.etree.ElementTree as etree
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

conj = 0
verb = 0

for token in root.iter('token'):
    word = token.get('text')
    if word.lower() == 'может':
        for g in token.iter('g'):
            if g.get('v') == 'CONJ':
                conj += 1
            elif g.get('v') == 'VERB':
                verb += 1
print(conj, 'союзов')
print(verb, 'глагола')
