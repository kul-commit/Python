class Account:
    def __init__(self, balance, account_no):
        self.balance= balance
        self.account_no= account_no

    def debit(self, amount):
          self.balance -= amount
          print(f"Rs. {amount} is debited")
          print("total balance = ", self.get_balance)


    def credit(self, amount):
         self.balance += amount
         print(f" rs.{amount} is credited")
         print("total balance = ", self.get_balance)


    def get_balance(self):
         return self.balance
        


user1= Account(1000000, 9821734)
user1.credit(4000)
user1.debit(1000) 