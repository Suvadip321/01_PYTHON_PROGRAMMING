l = []
n = int(input("Enter size of the list: "))
for i in range(1, n+1):
  el = int(input(f"enter element {i}: "))
  l.append(el)
  
# print(f"Max = {max(l)}, Min = {min(l)}")

max_val = min_val = l[0]
for el in l:
  if el > max_val:
    max_val = el
  if el < min_val:
    min_val = el

print(f"Max = {max_val}, Min = {min_val}")
