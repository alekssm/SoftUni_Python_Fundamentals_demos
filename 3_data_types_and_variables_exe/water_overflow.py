num_of_lines = int(input())

current_tank_capacity = 0

for p in range (1, num_of_lines + 1):
    water_per_pour = int(input())
    if current_tank_capacity + water_per_pour > 255:
        print("Insufficient capacity!")
    else:
        current_tank_capacity += water_per_pour

print(current_tank_capacity)