def find_missing_number(nums, n):
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(nums)
  return expected_sum - actual_sum

nums = [1, 2, 3, 5]
n = 5
print(f"Missing number: {find_missing_number(nums, n)}")