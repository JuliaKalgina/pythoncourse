import json
import collections

char_lines = collections.Counter()
with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    for act in data["acts"]:
        for scene in act["scenes"]:
            for action in scene["action"]:
                char_lines[action['character']] += 1
print(char_lines)
