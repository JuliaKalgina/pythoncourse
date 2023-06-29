import json
import collections
from collections import defaultdict

dd = collections.defaultdict(list)
with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    for act in data["acts"]:
        for scene in act["scenes"]:
            for action in scene["action"]:
                dd[action['character']].append(action['says'])
print(dd)
