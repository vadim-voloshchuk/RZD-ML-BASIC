from bank_menagment import SavingsAccount, CheckingAccount

class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, holder_name, account_type):
        account_number = len(self.accounts) + 1
        if account_type == "saving":
            account = SavingsAccount(account_number, holder_name)
        elif account_type == "checking":
            account = CheckingAccount(account_number, holder_name)
        else:
            ValueError("Неизвестный тип счёта")
        
        self.accounts.append(account)
    
    def close_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Счёт с номером {account_number} был удалён")
                return
        
        print("Счёта с таким номером нет в банке")

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account_by_number(from_account_number)
        to_account = self.get_account_by_number(to_account_number)

        if from_account and to_account:
            from_account.withdraw(amount)
            to_account.deposit(amount)

            print(f"Успешный перевод со счёта {from_account_number} на счёт {to_account_number}")
        else:
            print("Номера счетов неккоректны")

    def get_account_by_number(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

if __name__ == "__main__":
    bank = Bank()
    bank.open_account("TEST1", 'saving')
    bank.open_account("TEST2", 'checking')

    bank.accounts[0].deposit(5000)

    bank.transfer(1,2, 6000)

    for acc in bank.accounts:
        print(acc)
