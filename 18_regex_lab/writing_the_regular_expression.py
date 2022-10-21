import re

reg = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

text = input()

x = re.findall(reg, text)
print(*x)