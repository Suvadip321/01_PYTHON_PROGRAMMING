def remove_punctuation(text):
  punctuations = '''
  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

  '''
  result = ""
  for char in text:
    if char not in punctuations:
      result += char
  return result

sample = input("Enter some texts: ")
print(remove_punctuation(sample))