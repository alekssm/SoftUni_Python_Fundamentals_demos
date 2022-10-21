days = int(input())
ppl = int(input())
energy = float(input())
water_per_person = float(input())
food_per_person = float(input())

water = days*ppl*water_per_person
food = days*ppl*food_per_person

enough_energy_power = True

for day in range(1, days+1):
    energy_loss = float(input())
    energy -= energy_loss
    if energy <= 0:
        enough_energy_power = False
        break
    if day % 2 == 0:
        energy += energy * 0.05
        water = water * 0.7
    if day % 3 == 0:
        food -= food/ppl
        energy += energy * 0.1

if enough_energy_power:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")