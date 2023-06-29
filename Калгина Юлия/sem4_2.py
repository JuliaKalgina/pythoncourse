import xml.etree.ElementTree as etree
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

the_list = []
for token in root.iter('token'):
    word = token.find('./tfr/v/l').get('t')
    attributes = []

    for g in token.iter('g'):
        attributes.append(g.get('v'))

    if ('NOUN' in attributes) and ('plur' in attributes) and (word not in the_list):
        the_list.append(word)

with open('z2.txt', 'w', encoding='utf-8') as f:
    for i in the_list:
        f.write(i + '\n')
