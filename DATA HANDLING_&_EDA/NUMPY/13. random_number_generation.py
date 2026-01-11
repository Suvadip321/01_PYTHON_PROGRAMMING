import numpy as np 

np.random.seed(42) # for reproducibility

print(f"5 random integers [1, 10):\n{np.random.randint(1, 10, 5)}")
print(f"uniform distribution [0, 1) (5 samples):\n{np.random.uniform(0, 1, 5)}")
print(f"normal distribution (mean = 0, std = 1, 10 samples):\n{np.random.normal(0, 1, 10)}")
print(f"binomial distribution (n = 10, p = 0.5):\n{np.random.binomial(10, 0.5, 5)}")
print(f"exponential distribution (scale = 2):\n{np.random.exponential(2, 5)}")

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sample = np.random.choice(data, size=5, replace=False)
print(f"random sample: {sample}")
copied_data = data.copy()
np.random.shuffle(copied_data)
print(f"shuffled sample: {copied_data}")
