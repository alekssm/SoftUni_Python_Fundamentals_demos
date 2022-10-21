import re
pat = r"reb"

text = "rebel"

x = re.findall(pat, text)
print(x)