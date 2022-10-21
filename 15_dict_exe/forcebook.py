force = {}

while True:
    info = input()
    if info == "Lumpawaroo":
        break

    if "|" in info:
        side, user = info.split(" | ")

        for k, v in force.items():
            if user in v:
                continue

        if side not in force:
            force[side] = []
        force[side].append(user)

    elif "->" in info:
        user, side = info.split(" -> ")

        for k, v in force.items():
            if user in v:
                force[k].remove(user)

        if side not in force:
            force[side] = []
        force[side].append(user)
        print(f"{user} joins the {side}!")

for (k, v) in sorted(force.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
    if v:
        print(f"Side: {k}, Members: {len(v)}")
        for u in sorted(v):
            print(f"! {u}")
