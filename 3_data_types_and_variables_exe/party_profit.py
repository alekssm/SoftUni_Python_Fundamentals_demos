import math

start_party_members = int(input())
days_of_adventure = int(input())

current_coins_earned = 0
companions_of_party = start_party_members
for day in range (1, days_of_adventure + 1):
    current_coins_earned += 50
    if day % 10 == 0:
        companions_of_party -= 2
    if day % 15 == 0:
        companions_of_party += 5
    current_coins_earned -= 2 * companions_of_party
    if day % 3 == 0:
        current_coins_earned -= 3 * companions_of_party
    if day % 5 == 0:
        current_coins_earned += 20 * companions_of_party
        if day % 3 == 0:
            current_coins_earned -= 2 * companions_of_party

coins_per_member = math.trunc(current_coins_earned / companions_of_party)

print(f"{companions_of_party} companions received {coins_per_member} coins each.")