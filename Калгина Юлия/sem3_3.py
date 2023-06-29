import json

with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)
characters = {}
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            if action["character"] not in characters:
                characters[action["character"]] = 1
            else:
                characters[action["character"]] += 1
maximum_lines = 0
character_name = ""
for character in characters:
    if characters[character] >= maximum_lines:
        maximum_lines = characters[character]
        character_name = character
print(character_name)
