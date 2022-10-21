pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_hp_section = int(input())

command = input()
stale = True

while not command == "Retire":
    com_list = command.split()

    if len(com_list) == 3:
        action = com_list[0]
        index = int(com_list[1])
        points = int(com_list[2])
    elif len(com_list) == 4:
        action = com_list[0]
        index_1 = int(com_list[1])
        index_2 = int(com_list[2])
        points = int(com_list[3])
    else:
        action = com_list[0]

    if action == "Fire":
        if index < len(warship):
            warship[index] -= points
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                stale = False
                break
    elif action == "Defend":
        if index_1 < len(pirate_ship) and index_2 < len(pirate_ship):
            for ind in range(index_1, index_2 + 1):
                pirate_ship[ind] -= points
                if pirate_ship[ind] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stale = False
                    break
    elif action == "Repair":
        if index < len(pirate_ship):
            pirate_ship[index] += points
            if pirate_ship[index] > max_hp_section:
                pirate_ship[index] == max_hp_section
    elif action == "Status":
        count = 0
        for ele in pirate_ship:
            if ele < max_hp_section * 0.2:
                count += 1
        print(f"{count} sections need repair.")

    if not stale:
        break
    command = input()

if stale:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")