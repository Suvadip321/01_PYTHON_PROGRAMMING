# def unique_elements(l1, l2):
#   s1, s2 = set(l1), set(l2)
#   return list(s1 ^ s2)

def unique_elements(l1, l2):
  u = []
  for el in l1:
    if el not in l2 and el not in u:
      u.append(el)
  for el in l2:
    if el not in l1 and el not in u:
      u.append(el)
  
  return u

list1 = [1,2,3,4,5]
list2 = [4,5,6,7]
print(unique_elements(list1, list2))

