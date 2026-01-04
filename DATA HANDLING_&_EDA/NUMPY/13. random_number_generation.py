import numpy as np 

np.random.seed(42) # for reproducibility

print(f"5 random integers [1, 10): {np.random.randint(1, 10, 5)}")
print(f"5 random floats [0, 1): {np.random.random(5)}")
print(f"3 x 4 random matrix: {np.random.random((3, 4))}")
print(f"normal distribution (mean = 0, std = 1, 10 samples):\n{np.random.normal(0, 1, 10)}")
print(f"binomial distribution (n = 10, p = 0.5):\n{np.random.binomial(10, 0.5, 5)}")
print(f"exponential distribution (scale = 2): {np.random.exponential(2, 5)}")

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sample = np.random.choice(data, size=5, replace=False)
print(f"random sample: {sample}")
copied_data = data.copy()
np.random.shuffle(copied_data)
print(f"shuffled sample: {copied_data}")