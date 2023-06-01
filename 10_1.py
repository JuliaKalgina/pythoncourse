class Hooman:
    def __init__(self, cat, name, items):
        self.cat = cat
        self.name = name
        self.items = items

    def get_food(self):
        self.cat.is_hungry = False


class Cat:
    def __init__(self, name):
        self.name = name
        self.is_hungry = True


Gr = Cat('Garfield')
Pete = Hooman(Gr, 'Peter', 'food')
Pete.get_food()
print(Gr.is_hungry)
