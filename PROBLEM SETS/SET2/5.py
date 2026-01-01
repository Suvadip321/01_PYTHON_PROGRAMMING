# def revList(l):
#   return l[::-1]

def revList(l):
  n = len(l)
  for i in range(n // 2):
    l[i], l[n - i - 1] = l[n - i - 1], l[i]
  return l

    

l = [1,3,5,7,9]
revList(l)
print(l)
