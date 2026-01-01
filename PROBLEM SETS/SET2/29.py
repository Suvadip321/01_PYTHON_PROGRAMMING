def merge_dict(d1, d2):
  merged = d1.copy()
  for key, val in d2.items():
    if key in merged:
      merged[key] += val
    else:
      merged[key] = val
  return merged

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 25}

result = merge_dict(d1, d2)
print(result)
