import json

dictionary = {}
with open('wikidata_1000.json', 'r', encoding='utf8') as f:
    for lll in f:
        data = json.loads(lll)
        word = data['label']['value']
        if 'description' in data:
            brb = data['description']['value']
        else:
            brb = 'None'
        dictionary[word] = brb
