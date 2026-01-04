import pandas as pd 

data = [10, 20, 30, 40, 50]
series = pd.Series(data)
indexed_series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

print(f"series:\n{series}")
print(f"indexed_series:\n{indexed_series}")

dict_data = {'Apple': 5, 'Banana': 3, 'Orange': 8, 'Mango': 7, 'Pineapple': 10}
dict_series = pd.Series(dict_data)

print(f"dict_series:\n{dict_series}")

print("loc and iloc:")
print(f"loc: {dict_series.loc['Apple']}")
print(f"iloc: {dict_series.iloc[0]}")

# dict_series.iloc[2] = 8
# print(dict_series)

# print(dict_series[dict_series >= 7])