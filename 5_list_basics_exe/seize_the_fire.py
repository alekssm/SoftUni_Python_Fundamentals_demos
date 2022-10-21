info_for_fire = input()
water = int(input())

fire_list = info_for_fire.split("#")
print("Cells:")

total_fire = 0
total_effort = 0
water_left = water
for ele in fire_list:
    ele_list = ele.split(" = ")
    level = ele_list[0]
    value = int(ele_list[1])

    if "High" in ele_list:
        if 81 <= value <= 125 and value <= water_left:
            water_left -= value
            total_fire += value
            current_effort = value * 0.25
            total_effort += current_effort
            print(f" - {value}")

    if "Medium" in ele_list and value <= water_left:
        if 51 <= value <= 80:
            water_left -= value
            total_fire += value
            current_effort = value * 0.25
            total_effort += current_effort
            print(f" - {value}")

    if "Low" in ele_list and value <= water_left:
        if 1 <= value <= 50:
            water_left -= value
            total_fire += value
            current_effort = value * 0.25
            total_effort += current_effort
            print(f" - {value}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")