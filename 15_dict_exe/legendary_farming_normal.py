weapons = {
    "Shadowmourne": "shards",
    "Valanyr": "fragments",
    "Dragonwrath": "motes",
}

required_mats = {
    "shards": 0,
    "fragments": 0,
    "motes": 0,
}


mats = {}
done = False

while True:
    mats_data = input().lower().split()
    if done:
        break

    for i in range(0, len(mats_data), 2):
        if done:
            break

        current_quantity = int(mats_data[i])
        current_item = mats_data[i+1]

        if current_item not in mats:
            mats[current_item] = 0
        mats[current_item] += current_quantity

        if current_item in required_mats:
            required_mats[current_item] += current_quantity

        for item in required_mats:
            if required_mats[item] >= 250:

                for k, v in weapons.items():
                    if item == v:
                        print(f"{k} obtained!")
            done = True
            break
