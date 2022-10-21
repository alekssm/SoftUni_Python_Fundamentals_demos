num_of_defeats = int(input())
helm_repair_price = float(input())
sword_repair_price = float(input())
shield_repair_price = float(input())
armor_repair_price = float(input())

shield_repair_count = 0
whole_repair_gold = 0

for defeat in range (1, num_of_defeats + 1):
    if defeat % 2 == 0:
        whole_repair_gold += helm_repair_price
    if defeat % 3 == 0:
        whole_repair_gold += sword_repair_price
    if defeat % 2 == 0 and defeat % 3 == 0:
        whole_repair_gold += shield_repair_price
        shield_repair_count += 1
    if shield_repair_count == 2:
        whole_repair_gold += armor_repair_price
        shield_repair_count = 0

print(f"Gladiator expenses: {whole_repair_gold:.2f} aureus")