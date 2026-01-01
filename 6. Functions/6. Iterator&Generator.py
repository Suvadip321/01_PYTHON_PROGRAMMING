# ================= ITERATOR =================
nums = [1, 2, 3]        # A list is iterable
it = iter(nums)         # Convert iterable -> iterator
print(next(it))         # 1
print(next(it))         # 2
print(next(it))         # 3

# ================= GENERATOR =================
def my_gen():
  for i in range(1, 4):
    yield i             # yield pauses and returns value one by one

g = my_gen()            # Generator is also an iterator
print(next(g))          # 1
print(next(g))          # 2
print(next(g))          # 3
