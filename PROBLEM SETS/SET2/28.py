# def remove_none(l):
#   return [x for x in l if x != None]

def remove_none(l):
  return [x for x in l if x is not None]

data = [1, None, 5, None, 6]
cleaned = remove_none(data)
print(f"Original List: {data}")
print(f"List without None: {cleaned}")