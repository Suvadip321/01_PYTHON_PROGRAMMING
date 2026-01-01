def armstrong(a, b):
  l = []
  for i in range(a, b+1):
    n = str(i)
    d = len(n)
    x = 0
    for j in n:
      x += (int(j))**d
    if i == x:
      l.append(i)
      
  return(l)

# def armstrong(a, b):
#     return [i for i in range(a, b+1) if i == sum(int(d)**len(str(i)) for d in str(i))]

a = armstrong(1, 1000)
print(a)

