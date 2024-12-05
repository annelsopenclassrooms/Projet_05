## Écrivez votre code ici !
class BankAccount:

    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):

        if amount < 0:
            print("Le montant doit être positif")
            pass
        else:
            self.balance = self.balance + amount

    def withdraw(self, amount):

        if amount < 0:
            print("Le montant doit être positif")
            pass

        elif amount > self.balance:
            print("Votre solde est insuffisant")
            pass

        else:
            self.balance = self.balance - amount

    def display_balance(self):
        print(f"Votre solde est de : {self.balance}")



ba = BankAccount("Anne", 1300)

ba.deposit(100)

ba.display_balance()

ba.withdraw(1500)

ba.display_balance()

ba.withdraw(500)

ba.display_balance()