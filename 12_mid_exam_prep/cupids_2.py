neighbourhood = list(map(int, input().split("@")))
command = input()

position = 0

while not command == "Love!":
    jump_com_list = command.split()
    jump_len = int(jump_com_list[1])

    position += jump_len
    if position >= len(neighbourhood):
        position = 0

    if neighbourhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighbourhood[position] -= 2
        if neighbourhood[position] <= 0:
            print(f"Place {position} has Valentine's day.")
            neighbourhood[position] = 0

    command = input()

print(f"Cupid's last position was {position}.")

count = 0
for ele in neighbourhood:
    if not ele == 0:
        count += 1

if count == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count} places.")
