def mergeDict(d1, d2):
  return d1|d2

dict1 = {
  "x": 1,
  "y": 2
}

dict2 = {
  "y": 3,
  "z": 4
}

dict3 = mergeDict(dict1, dict2)
print(dict3)