# Encapsulation = bundling data (attributes) and methods together in a class and restricting direct access to some variable. We achieve this using Access Modifiers:
# Public attributes: accessible everywhere
# Protected attributes: conventionally restricted (prefix _)
# Private attributes: strictly hidden (prefix __), accessible only via methods

class BankAccount:
  def __init__(self, account_number, balance):
    self.account_number = account_number     # public attribute
    self._account_type = "Savings"     # protected attribute (same to public attribute in python)
    self.__balance = balance     # private attribute
    
  # getter method for private balance
  def get_balance(self):
    return self.__balance
  
  # setter method with validation
  def deposit(self, amount):
    if(amount > 0):
      self.__balance += amount
      print(f"Deposited {amount}. Balance: {self.__balance}")
    else:
      print("Invalid deposit amount!")
      
  def withdraw(self, amount):
    if 0 < amount <= self.__balance:
      self.__balance -= amount
      print(f"Withdrawn {amount}. Balance: {self.__balance}")
    else:
      print("Invalid withdraw amount!")
      
      
      
# create account
acc = BankAccount("12345", 1000)

# public attribute: directly accessible
print(acc.account_number)

# protected attribute: accessible but not recommended
print(acc._account_type)

# private attribute: not directly accessible
# print(acc.__balance)

# access using getter
print(acc.get_balance())

# modify safely using methods
acc.deposit(500)
acc.withdraw(750)