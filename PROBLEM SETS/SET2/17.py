def countVowels(s):
  count = 0
  for i in s.lower():
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
      count += 1
  return count

string = input("Enter a string: ")
print(countVowels(string))