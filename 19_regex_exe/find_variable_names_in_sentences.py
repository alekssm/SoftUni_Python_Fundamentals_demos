import re

pattern = r"\b\_(?P<v_n>[A-Za-z0-9]+)\b"
text = input()
res = []

matches = re.finditer(pattern, text)
for match in matches:
    res.append(match.group("v_n"))


print(','.join(res))