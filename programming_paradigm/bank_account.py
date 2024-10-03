class BankAccount:
  
  def __init__(self, account_balance, balance=0):
    self.account_balance = account_balance
    self._balance = balance
    
  def deposit(self, amount):
    if amount > self._balance:
      self._balance = self.account_balance
      return {amount}
    
  
  def withdraw(self, amount):
    if amount < self.account_balance:
      self.account_balance -= amount
      return True
    else:
      return False 
  
  def display_balance(self):
    print(f"Current Balance: ${self.account_balance:.2f}")