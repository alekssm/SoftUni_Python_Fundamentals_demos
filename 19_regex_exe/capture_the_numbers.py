import re

reg = r"\d+"
text = input()
regs = []

while text:
    x = re.findall(reg, text)
    regs.extend(x)
    text = input()
print(*regs)