import re

text = input().lower()
word = input().lower()
pattern = rf"\b{word}\b"

res = re.findall(pattern, text)

print(len(res))