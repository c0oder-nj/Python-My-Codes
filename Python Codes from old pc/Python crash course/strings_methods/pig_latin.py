def pig_latin(text):
  say = text.split()
  # Separate the text into words
  pigLatin = []
  for word in say:
    newword = ""
    newword = word[1:] + word[0] + "ay "
    pigLatin.append(newword)
# Turn the list into string
  liTostr = ""
  for word in pigLatin:
    liTostr += word
  return liTostr
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"