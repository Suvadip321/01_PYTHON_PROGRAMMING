# def format(text):
#   return " ".join(word.capitalize() for word in text.split())

def format(text):
  words = text.split()
  result = []
  for word in words:
    result.append(word.capitalize())
  return " ".join(result)


text = " supreme    kNowledge foundation  "
print(format(text))