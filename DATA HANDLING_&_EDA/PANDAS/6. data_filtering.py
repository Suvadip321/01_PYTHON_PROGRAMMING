import pandas as pd 

df = pd.read_csv('IPL2025Batters.csv')

print("top runs:")
top_runs = df[df['Runs'] >= 500]
print(top_runs)

print("top strike rates:")
top_sr = df[df['SR'] >= 150]
print(top_sr)

print("top runs and strike rates:")
top_rsr = df[(df['Runs'] >= 500) & (df['SR'] >= 150)]
print(top_rsr)

print("top runs and strike rates using loc:")
top_rsr = df.loc[
    (df['Runs'] >= 500) & (df['SR'] >= 150)
]
print(top_rsr)
