class Beast:
    def __init__(self):
        self.age = 12
        self._fangs = 'sharp'
        self.__nose = 'boopable'

    def info_card(self):
        print(self._fangs)
        print(self.__nose)


Wolf = Beast()
print(Wolf.age)
Wolf.age = 20
print(Wolf.age)
Wolf.info_card()
