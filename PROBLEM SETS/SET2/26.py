def rotate_left(l, k):
  n = len(l)
  k = k % n
  return l[k:] + l[:k]

def rotate_right(l, k):
  n = len(l)
  k = k % n
  return l[-k:] + l[:-k]

nums = [1, 2, 3, 4, 5]
print(rotate_left(nums, 2))
print(rotate_right(nums, 2))
