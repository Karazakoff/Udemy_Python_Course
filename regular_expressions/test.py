import re
text = "yes. you do this shoot!, and give me your phone number soon or later phone previous"
pattern = 'phone'
match = re.search(pattern, text)
print(match.span())
print(match.group())
print(match.start())
print(match.end())
matches = re.findall(pattern, text)
print(matches)
print(len(matches))

for match in re.finditer(pattern, text):
    print(match.span())
    
