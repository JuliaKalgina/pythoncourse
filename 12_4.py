class Genie:
    def __init__(self, name, wishes, curse, phrase):
        self.name = name
        self.wishes = wishes
        self.__curse = curse
        self.lift_phrase_curse = phrase

    def lift_the_curse(self):
        the_lift_phrase_curse = input('Say the special phrase to lift my curse!')
        if the_lift_phrase_curse == self.lift_phrase_curse:
            print('The ' + self.__curse + ' curse is lifted!')
        else:
            print('I am still trapped and cursed.')

    def acquire_curse(self, new_curse):
        if len(new_curse) > 0:
            self.__curse = new_curse

    def show_curse(self):
        return self.__curse

    def grant_wish(self):
        a_wish = input('Wish for something: ')
        if len(a_wish) > 0:
            self.wishes -= 1
            print('Wish granted')


Genieee = Genie('Geralt', 3, 'always sneezes', 'I free you')
Genieee.grant_wish()
print(Genieee.wishes)
Genieee.lift_the_curse()
Genieee.acquire_curse("talks very slowly")
print(Genieee.show_curse())

