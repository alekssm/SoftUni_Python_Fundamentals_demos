metals = {}

current_metal = ''
line = 1

while True:
    command = input()
    if command == "stop":
        break

    if line % 2 != 0:
        current_metal = command
    else:
        if current_metal not in metals:
            metals[current_metal] = 0
        metals[current_metal] += int(command)

    line += 1

for k, v in metals.items():
    print(f"{k} -> {v}")
