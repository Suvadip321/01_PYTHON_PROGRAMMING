import csv

with open("data.csv", mode="r") as f:
  reader = csv.reader(f)
  for row in reader:
    print(row)
