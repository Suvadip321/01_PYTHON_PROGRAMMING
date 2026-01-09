# ITERATOR
nums = [1, 2, 3]
i = iter(nums)
print(i)
print(next(i))         # 1
print(next(i))         # 2
print(next(i))         # 3

# GENERATOR
def my_gen():
  for i in range(1, 4):
    yield i             # yield pauses and returns value one by one

gen = my_gen()            # Generator is also an iterator
print(gen)
print(next(gen))          # 1
print(next(gen))          # 2
print(next(gen))          # 3
