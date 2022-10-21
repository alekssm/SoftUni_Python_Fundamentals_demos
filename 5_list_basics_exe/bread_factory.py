working_event_daily = input()
working_event_list = working_event_daily.split("|")

energy = 100
coins = 100
out_of_coins = False

for event in working_event_list:
    event_list = event.split("-")
    type_of_event = event_list[0]
    energy_or_coins = int(event_list[1])

    if "rest" in event:
        if energy + energy_or_coins < 100:
            energy += energy_or_coins
            print(f"You gained {energy_or_coins} energy.")
            print(f"Current energy: {energy}.")
        else:
            diff = 100 - energy
            print(f"You gained {diff} energy.")
            energy = 100
            print(f"Current energy: {energy}.")
    elif "order" in event:
        if energy - 30 >= 0:
            energy -= 30
            coins += energy_or_coins
            print(f"You earned {energy_or_coins} coins.")
        else:
            if energy + 50 < 100:
                energy += 50
                print("You had to rest!")
            else:
                energy = 100
                print("You had to rest!")
    else:
        if coins - energy_or_coins > 0:
            coins -= energy_or_coins
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            out_of_coins = True
            break

if not out_of_coins:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
