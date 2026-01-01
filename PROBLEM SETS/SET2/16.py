def isPalindrome(s):
  return s == s[::-1]

string = input("Enter a string: ")
print(isPalindrome(string))