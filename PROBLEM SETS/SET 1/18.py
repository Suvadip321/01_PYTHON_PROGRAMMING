while(True):
  c = input("Enter a character: ").lower()
  if c.isalpha() and len(c) == 1:
    if c in "aeiou":
      print("Vowel")
    else:
      print("Consonant")
  else:
    print("Please enter a valid input.")