line_count = 0
word_count = 0

with open("sample.txt", "r") as f:
  for line in f:
    line_count += 1
    word_count += len(line.split())
    
print(f"No of lines: {line_count}")
print(f"No of words: {word_count}")