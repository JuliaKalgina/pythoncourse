class BankAccount:
    def __init__(self, name, number, balance, password):
        self.holders_name = name
        self.account_number = number
        self.__balance = balance
        self.__password = password

    def change_the_balance(self, ch):
        in_password = input('Enter your password here:')
        if in_password == self.__password:
            self.__balance = ch
            print('You just changed the balance to' + str(ch))
        else:
            print('You entered the wrong password')


BBBankAccount = BankAccount('Julio', 911, 8888, 'WhoLetTheDogsOut')
BBBankAccount.change_the_balance(4242)