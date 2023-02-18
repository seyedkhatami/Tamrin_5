class BankAccount:

    def __init__(self, date_of_opening, account_number, customer_name):

        self.__date_of_opening = date_of_opening
        self.__account_number = account_number
        self.__customer_name = customer_name

#encapsulation
#date_of_opening
    @property
    def date_of_opening(self):
        return self.__date_of_opening
    
    @date_of_opening.setter
    def date_of_opening(self, value):
        self.__date_of_opening = value

    @date_of_opening.deleter
    def date_of_opening(self):
        del self.__date_of_opening

#account_number
    @property
    def account_number(self):
        return self.__account_number
    
    @account_number.setter
    def account_number(self, value):
        self.__account_number = value

    @account_number.deleter
    def account_number(self):
        del self.__account_number

#customer_name
    @property
    def customer_name(self):
        return self.__customer_name
    
    @customer_name.setter
    def customer_name(self, value):
        self.__customer_name = value

    @customer_name.deleter
    def customer_name(self):
        del self.__customer_name

#methods
    def withdraw(self):
        pass

    def deposit(self):
        pass

    def check_balance(self):
        pass



a = BankAccount("2022.05.01", "9198985549", "Ali")
a.deposit()
a.withdraw()
a.check_balance()
