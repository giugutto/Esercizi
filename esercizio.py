alphabet = ["a","b","c","d","e"]
print(alphabet)
first_letter = "a"
last_letter = "e"

first_three = alphabet[3:]
print(first_three)
last_three = alphabet[-3:]
alphabet.append("f")
alphabet.append("g")
alphabet.append("h")
print(alphabet)

last_three = (alphabet[-3:])
print(last_three)
alphabet.pop(-1)
print(alphabet)