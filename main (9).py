class BankAccount:
    def __init__(self, account_number,customer_name, balance ):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(amount," has been deposited in your account.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(amount," has been withdrawn from your account.")
            
    def check_balance(self):
        print("Current balance is ",self.balance)
        
    def print_customer_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Balance: ",self.balance)   

obj1 = BankAccount(2345,"Thariq",1000 )
print("Customer Details:")
obj1.print_customer_details()
obj1.deposit(1000)
obj1.check_balance()
obj1.withdraw(500)
obj1.check_balance()