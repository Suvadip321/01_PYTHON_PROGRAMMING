def count_freq(l):
  freq = {}
  for el in l:
    if el in freq:
      freq[el] += 1
    else:
      freq[el] = 1
  return freq

nums = [1,3,4,2,4,2,5,7,8,6,5,0,1,9,8]
print(count_freq(nums))