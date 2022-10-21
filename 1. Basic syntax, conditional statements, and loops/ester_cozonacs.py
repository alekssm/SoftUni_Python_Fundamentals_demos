import math
from math import floor

budget = float(input())
kg_flour_price = float(input())
one_eggs_pack_price = kg_flour_price * 0.75
one_liter_milk_price = kg_flour_price + kg_flour_price * 0.25
milk_for_one_cozonac_price = one_liter_milk_price / 4

price_for_one_cozonac = kg_flour_price + one_eggs_pack_price + milk_for_one_cozonac_price
all_cozonacs_made = floor(budget / price_for_one_cozonac)
money_left = budget - (price_for_one_cozonac * all_cozonacs_made)
received_eggs = 0
cozonacs_count = 0
for i in range (1, all_cozonacs_made + 1):
    received_eggs += 3
    cozonacs_count += 1
    if cozonacs_count == 3:
        received_eggs = received_eggs - (i - 2)
        cozonacs_count = 0

print(f"You made {all_cozonacs_made} cozonacs! Now you have {received_eggs} eggs and {money_left:.2f}BGN left.")