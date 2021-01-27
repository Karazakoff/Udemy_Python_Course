import re

print(re.findall(r"cat|dog", "The cat is here and dog is there"))

print(re.findall(r"...at", "The cat sat somewhere there with hat and went splat"))

print(re.findall(r"^\d", "2 is a number."))

print(re.findall(r"\d$", "The number is 2"))

phrase = "There are 3 numbers with 34 in 5 sentence"

pattern = r'[^\d]+'

print(re.findall(pattern, phrase))

phrase = "This is a string. But it has punctuations! How can we remove it?"

pattern = r'[^?.! ]+'

print(re.findall(pattern, phrase))

text = re.findall(pattern, phrase)

print(" ".join(text))

text = "Hy my-dear we would like to show-you, something! it calls besh-barmak"

pattern = r"[\w]+-[\w]+"

print(re.findall(pattern, text))

text_one = "Hello, would you like to buy a catfish?"
text_two = "Hello, would you like to buy a catnap?"
text_three = "Hello, would you like to buy a caterpiller"

print(re.findall(r"cat(fish|nap|erpiller)", text_one))
print(re.findall(r"cat(fish|nap|erlipper)", text_two))
print(re.findall(r"cat(fish|nap|erpiller)", text_three))
