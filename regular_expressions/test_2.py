import re

text = "Hello my phone number is +996-(778)-892-312"
pattern = r"\+\d{3}-\((\d{3})\)-\d{3}-\d{3}"
match = re.search(pattern, text)
print(match.group())
phone_patterns = re.compile(r"(\+\d{3})-(\((\d{3})\))-(\d{3})-(\d{3})")
results = re.search(phone_patterns, text)
print(results.group(1))
print(results.group(2))
print(results.group(3))
print(results.group(4))
print(results.group(5))
