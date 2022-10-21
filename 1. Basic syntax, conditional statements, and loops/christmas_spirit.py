allowed_quantity = int(input())
days_till_christmas = int(input())

ornament_set_price_per_one = 2
tree_skirt_price_per_one = 5
tree_garlands_price_per_one = 3
tree_lights_price_per_one = 15


quantity = allowed_quantity
total_spirit = 0
total_cost = 0

for day in range(1, days_till_christmas + 1):
    ornament_set_price = 2 * quantity
    tree_skirt_price = 5 * quantity
    tree_garlands_price = 3 * quantity
    tree_lights_price = 15 * quantity
    if day % 2 == 0:
        total_spirit += 5
        total_cost += ornament_set_price
    if day % 3 == 0:
        total_spirit += 13
        total_cost += tree_skirt_price + tree_garlands_price
    if day % 5 == 0:
        total_spirit += 17
        total_cost += tree_lights_price
    if day % 3 == 0 and day % 5 == 0:
        total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price_per_one + tree_garlands_price_per_one + tree_lights_price_per_one
        quantity += 2

if days_till_christmas % 10 == 0:
        total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")