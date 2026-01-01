l = []
n = int(input("Enter size of the list: "))
for i in range(1, n+1):
  l.append(int(input(f"Enter element {i}: ")))
  
print(f"Your list is: {l}")
print(f"Total sum of the list elements = {sum(l)}")