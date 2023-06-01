class Employee:
    def __init__(self, name):
        self.name = name
        self.position = self.__class__.__name__

    def card(self):
        print(self.name + ' works as a ' + self.position)


class FinancesEmployee(Employee):
    def __init__(self, name):
        super().__init__(name)


class CommunicationsEmployee(Employee):
    def __init__(self, name):
        super().__init__(name)


class FundraisingEmployee(Employee):
    def __init__(self, name):
        super().__init__(name)


class FinanceSpecialist(FinancesEmployee):
    def __init__(self, name):
        super().__init__(name)


class FinanceDirector(FinancesEmployee):
    def __init__(self, name):
        super().__init__(name)


class CommunicationsSpecialist(CommunicationsEmployee):
    def __init__(self, name):
        super().__init__(name)


class CommunicationsDirector(CommunicationsEmployee):
    def __init__(self, name):
        super().__init__(name)


class FundraisingSpecialist(FundraisingEmployee):
    def __init__(self, name):
        super().__init__(name)


Lola = FinanceDirector('Lola Chance')
Charlie = FinanceSpecialist('Charlie Anderson')
Wes = FundraisingSpecialist('Wes Johnson')
Tony = CommunicationsDirector('Tony Brotherinchrist')
Ezekiel = CommunicationsSpecialist('Ezekiel Tonyhater')


Lola.card()
Charlie.card()
Wes.card()
Tony.card()
Ezekiel.card()

