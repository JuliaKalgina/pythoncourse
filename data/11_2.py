class Figures:
    def __init__(self):
        self.colour = "white"

    def change_the_colour(self, diff_colour):
        self.colour = diff_colour

    def output(self):
        print(self.colour)


class Oval(Figures):
    def __init__(self):
        super().__init__()
        self.figname = 'oval'

    def output(self):
        print(self.colour, self.figname)


class Square(Figures):
    def __init__(self):
        super().__init__()
        self.figname = 'square'

    def output(self):
        print(self.colour, self.figname)
