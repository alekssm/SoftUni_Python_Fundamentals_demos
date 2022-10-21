import re

pattern = r"\s(?P<email>(?P<user>[A-Za-z0-9]+[A-Za-z0-9\.\-\_]*)\@(?P<host>[A-Za-z]+[A-Za-z\-]*(\.[A-Za-z]+[A-Za-z\-]*)+))\b"
text = input()

res = re.finditer(pattern, text)
for match in res:
    print(match.group("email"))