import numpy as np 

data = np.array([1.0, 2.0, np.nan, 4.0, np.nan, 6.0])

is_NaN = np.isnan(data)
print(f"is_NaN: {is_NaN}")

nan_count = np.sum(is_NaN)
print(f"NaN_count: {nan_count}")

clean_data = data[~is_NaN]
print(f"clean_data: {clean_data}")

filled_data = np.nan_to_num(data, nan=0)
print(f"filled_data: {filled_data}")

print(f"sum (ignoring NaN): {np.nansum(data)}")
print(f"mean (ignoring NaN): {np.nanmean(data)}")