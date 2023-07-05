
# Create a User class with an __init__ method.
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)



# other methods


# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
        self.account.deposit()
        print(self.account.amount)


# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdrawl(self, amount):
        self.account.withdrawal()
        print(self.account.amount)


# Add a display_user_balance method to the User class that displays user's account balance
    def  display_user_balance(self,):
        self.account.display()