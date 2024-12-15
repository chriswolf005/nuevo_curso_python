class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual: {self.balance}")
        else:
            print("No se puede depositar,la cuenta se encuentra inactiva")
    
    def withdraw(self,amount):
        if self.active:
            if amount <=self.balance:
                self.balance-=amount
                print(f"se ha retirado {amount}.Su saldo actual es {self.balance}")
            else:
                print("Tu cuenta no posee saldo suficiente para esta operacion")
        else:
            print("Tu cuenta esta desactivada")
    def deactivate_account(self):
        self.is_active=False
        print("Tu cuenta has sido desactivada")

    def activate_account(self):
        self.is_active=True
        print("Tu cuenta has sido activada")
    

cuenta_juan=BankAccount("Juan",500)

cuenta_carli=BankAccount("Carli",1000)

#Llamada a los metodos

cuenta_juan.deposit(200)
cuenta_carli.deposit(100)
cuenta_juan.deactivate_account()
cuenta_juan.deposit(50)