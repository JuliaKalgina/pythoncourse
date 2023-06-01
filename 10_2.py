class Warrior:
    def __init__(self, name, age, weapons):
        self.name = name
        self.age = age
        self.weapons_collection = weapons

    def collect_weapon(self, weapon: str):
        self.weapons_collection.append(weapon)


Elladan = Warrior('Elladan', 2988, ['crossbow', 'bow', 'knife'])
Elrohir = Warrior('Elrohir', 2988, ['bow', 'sword', 'dagger'])

Elladan.collect_weapon('dagger')
print(Elladan.weapons_collection)