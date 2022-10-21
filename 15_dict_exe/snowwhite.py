dwarfs = {}

while True:
    info = input()
    if info == "Once upon a time":
        break

    info_ll = info.split(" <:> ")

    name = info_ll[0]
    hat_color = info_ll[1]
    physics = int(info_ll[2])

    if name not in dwarfs:
        dwarfs[name] = {}
        dwarfs[name][hat_color] = physics

    else:
        if hat_color not in dwarfs[name]:
            dwarfs[name][hat_color] = physics
        else:
            if physics > dwarfs[name][hat_color]:
                dwarfs[name][hat_color] = physics

dwarfs_ll = []

for d, c in dwarfs.items():
    for hat, points in c.items():
        dwarfs_ll.append((d, hat, points))


# hat_colors = {}
#
# dwarfs_sp = sorted(dwarfs_ll, key=lambda k: -k[2])
#
# for x in dwarfs_sp:
#     if x[1] not in hat_colors:
#         hat_colors[x[1]] = 0
#     hat_colors[x[1]] += 1
#
# dwarfs_cl = []
# for x in dwarfs_sp:

for x in sorted(dwarfs_ll, key=lambda k: -k[2]):
    print(f"({x[1]}) {x[0]} <-> {x[2]}")
