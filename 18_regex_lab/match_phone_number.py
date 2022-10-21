import re

reg = r"\+359([\s-])2(\1)\d{3}(\1)\d{4}\b"
text = input()
res = re.finditer(reg, text)
res = [num.group() for num in res]
print(f'{", ".join(res)}')
