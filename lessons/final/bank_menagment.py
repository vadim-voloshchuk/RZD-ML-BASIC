class Account():
    def __init__(self,account_number, holder_name, balance=0, currency="RUB"):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.currency = currency

    def deposit(self,amount):
        self.balance += amount
        print(f"Зачислено: {amount} рублей")

    def withdraw(self,amount):
        self.balance -= amount
        print(f"Снято: {amount} рублей")

    def get_balance(self):
        return f"Ваш баланс: {self.balance}"

    def __str__(self):
        return f"Счёт {self.account_number} - {self.holder_name}, баланс: {self.balance} {self.currency}"

class SavingsAccount(Account):
    def __init__(self,account_number, holder_name, balance=0, currency="RUB"):
        super().__init__(account_number, holder_name, balance, currency)
        self.interest_rate = 0.05

    def set_interest_rate(self, rate):
        self.interest_rate = rate
        print(f"Ваша ставка: {self.interest_rate}")

    def calculate_interest(self):
        self.balance *= 1 + self.interest_rate 
        print(f"Ваш счет составляет: {self.balance}")

class CheckingAccount(Account) :
    def __init__(self,account_number, holder_name, balance=0, currency="RUB"):
        super().__init__(account_number, holder_name, balance, currency)
        self.transaction_limit = 50

    def deduct_fees(self) :
        self.balance -= 0.01
        self.transaction_limit -= 1
        print(f"Счeт после обслуживания: {self.balance}")

    def reset_transactions(self):
        self.transaction_limit = 50
        print(f"Количество транзакций равно{self.transaction_limit}")

if __name__ == "__main__":
    test_account = SavingsAccount("0000000", "TEST")
    print(test_account)
    test_account.deposit(5000)
    test_account.calculate_interest()
    test_account.deposit(2500)
    test_account.withdraw(3653)
    test_account.set_interest_rate(0.2)
    test_account.calculate_interest()
    test_account.get_balance()


