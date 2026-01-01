from random import randint
x = randint(1, 10)

print("welcome to number guessing game.\nYou have to guess the correct number between 1 to 10 within 5 attempts.")
a = 0
while(True):
  if a < 5:
    a += 1
    n = int(input("Enter the correct number: "))
    if n == x:
      print(f"Congratulations, You have guessed the correct number ({x}).\nAttempt No.: {a}")
      break
  else:
    print(f"Attempt limit reached.\nCorrect Number was {x}")
    break
  