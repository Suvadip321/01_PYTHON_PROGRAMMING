try:
  with open("file.txt") as f:
    print(f.read())
except FileNotFoundError:
  print("File not found!")