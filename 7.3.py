class Account:
    def __init__(self, id=0, balance=100.0, annualInterestRate=0.0):
        self.__id = int(id)
        self.__balance = float(balance)
        self.__annualInterestRate = float(annualInterestRate/100)

    #Getters (Accessors)

    def getID(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate/100

    #Setters(Accessors)

    def setID(self, id):
        self.__id = int(id)

    def setBalance(self, balance):
        self.__balance = float(balance)

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = float(annualInterestRate/100)

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate/12

    def getMonthlyInterest(self):
        return self.__balance*self.getMonthlyInterestRate()

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

def main():

    account = Account(1122, 20000, 4.5)
    account.withdraw(2500)
    account.deposit(3000)
    print("Account ID is:", account.getID())
    print("Monthly Interest Rate is:", account.getMonthlyInterestRate())
    print("Monthly Interest is:", account.getMonthlyInterest())
    print(f"Balance is: {account.getBalance():,.2f}")


main()




