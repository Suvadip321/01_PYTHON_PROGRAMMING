l1 = [1,3,4,2,4,2,5,7,8,6,5,0,1,9,8]
# l1 = list(set(l1))
# print(l1)
l2 = []
for el in l1:
  if el not in l2:
    l2.append(el)
    
l1 = l2
print(l1)