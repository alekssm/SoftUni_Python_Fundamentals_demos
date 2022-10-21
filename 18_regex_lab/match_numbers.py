import re

reg = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()

res = re.finditer(reg, text)
res = [num.group() for num in res]
print(*res)