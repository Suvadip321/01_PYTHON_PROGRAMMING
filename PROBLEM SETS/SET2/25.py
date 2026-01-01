def secMax(l):
  l = list(set(l))
  if len(l) < 2:
    return None
  l.sort(reverse=True)
  return l[1]

nums = [4,2,7,8,3]
print(secMax(nums))

