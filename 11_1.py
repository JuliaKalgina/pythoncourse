class Table:
    def __init__(self, l, w, h, obj):
        self.length = l
        self.width = w
        self.height = h
        self.objects = obj

    def outing(self):
        print(self.length, self.width, self.height, self.objects)


class Kitchen(Table):
    def howplaces(self, n):
        if n < 2:
            print("It is not a kitchen table")
        else:
            self.places = n

    def outplaces(self):
        print(self.places)


class Coffee(Table):
    def magazines_presence(self, obj):
        if obj == "magazine":
            print("That's a classic coffee table")
        else:
            print("That's not a classic coffee table")

    def height_check(self, w):
        if w > 3:
            print("It is too tall to be a coffee table")
        else:
            print("It is indeed a coffee table")


