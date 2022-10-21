import re

pattern = r"(?P<link>www\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)"

text = input()
new = ""
while text:
    new += text
    text = input()

res = re.finditer(pattern, new)

for match in res:
    print(match.group("link"))