import re

pattern = r"(?P<whole>\|(?P<name>[A-Z]{4,})\|\:\#(?P<title>[A-Za-z]+\s[A-Za-z]+)\#)"

num = int(input())

for n in range(num):
    text = input()
    res = re.finditer(pattern, text)
    for match in res:
        if match.group("whole") != "":
            name = match.group('name')
            title = match.group('title')
            print(f"{name}, The {title}")
            print(f">> Strength: {len(name)}")
            print(f">> Armor: {len(title)}")
