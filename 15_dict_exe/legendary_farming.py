mats = {}
weapons = {
    "Shadowmourne": "shards",
    "Valanyr": "fragments",
    "Dragonwrath": "motes",
}

# weapons = {
#     "Shadowmourne": {"shards": 0},
#     "Valanyr": {"fragments": 0},
#     "Dragonwrath": {"motes": 0},
# }

needed_mats = {
    weapons["Shadowmourne"]: 0,
    weapons["Valanyr"]: 0,
    weapons["Dragonwrath"]: 0,
}

done = False

while True:
    mats_data = input().lower().split()
    if done:
        break

    for i in range(0, len(mats_data), 2):

        current_item = mats_data[i+1]
        current_quantity = mats_data[i]

        if current_item not in mats and current_item not in needed_mats:
            mats[current_item] = 0
        if current_item not in needed_mats:
            mats[current_item] += int(current_quantity)

        if current_item in needed_mats:
            needed_mats[current_item] += int(current_quantity)

        for k, v in needed_mats.items():
            if v >= 250:
                needed_mats[k] -= 250
                for key, val in weapons.items():
                    if val == k:
                        print(f"{key} obtained!")
                        done = True
                        break
                break
        if done:
            break
    if done:
        break

for (k, v) in sorted(needed_mats.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{k}: {v}")
for (k, v) in sorted(mats.items(), key=lambda kvp: kvp[0]):
    print(f"{k}: {v}")
