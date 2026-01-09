# Encapsulation = bundling data (attributes) and methods together in a class and restricting direct access to some variable. We achieve this using Access Modifiers:
# Public attributes/methods : accessible everywhere
# Protected attributes/methods : conventionally restricted (prefix _) (but same as public attributes in python)
# Private attributes/methods : strictly hidden (prefix __), accessible only via methods

class BankAccount:
  def __init__(self, account_number, balance):
    self.account_type = "Savings"          # public attribute (accessible)
    self._account_number = account_number  # protected attribute (accessible, but not recommended)
    self.__balance = balance               # private attribute (not accessible)

  @property
  def balance(self):
    """Read-only access to balance"""
    return self.__balance
    
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
print(acc.account_type)

# protected attribute: accessible but not recommended
print(acc._account_number)

# private attribute: not directly accessible
# print(acc.__balance)

# modify and access safely using methods
acc.deposit(500)
acc.withdraw(750)
print(acc.balance)
