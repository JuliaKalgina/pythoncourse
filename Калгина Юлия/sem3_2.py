import json

with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)
dddata = []
for act in data["acts"]:
    for scene in act["scenes"]:
        characters = set()
        for action in scene["action"]:
            characters.add(action["character"])
        dddata.append(list(characters))

with open('final.json', 'w') as f:
    for line in dddata:
        f.write(json.dumps(line, ensure_ascii=False, separators=(',', ':')))
        f.write("\n")
