items = {}

info = input()

while not info == "statistics":
    list_of_info = info.split(": ")
    keys = list_of_info[0]
    val = int(list_of_info[1])
    if keys not in items:
        items[keys] = val
    else:
        items[keys] += val
    info = input()

print("Products in stock:")
for key in items:
    print(f"- {key}", end =": " )
    print(f"{items[key]}")

num = 0
for num_1 in items.values():
    num += num_1

print(f"Total Products: {len(items)}")
print(f"Total Quantity: {num}")