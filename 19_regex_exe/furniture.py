import re

pattern = r">>(?P<product>[A-Za-z]+)<<(?P<price>\d+(\.\d+)*)!(?P<quantity>\d+)"

text = input()
text_list = []
while not text == "Purchase":
    text_list.append(text)
    text = input()

text = ", ".join(text_list)

res = re.finditer(pattern, text)

money = 0
print("Bought furniture:")
for match in res:
    print(match.group("product"))
    money += (float(match.group("price"))) * int(match.group("quantity"))
print(f"Total money spend: {money:.2f}")