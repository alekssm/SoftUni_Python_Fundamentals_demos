contests = {}

users = {}

while True:
    info = input()
    if info == "no more time":
        break

    info_ll = info.split(" -> ")

    user = info_ll[0]
    contest = info_ll[1]
    points = int(info_ll[2])

    if contest not in contests:
        contests[contest] = {}
        contests[contest][user] = points

        if user not in users:
            users[user] = 0
        users[user] += points

    else:
        if user not in contests[contest]:
            contests[contest][user] = points

            if user not in users:
                users[user] = 0
            users[user] += points

        else:
            if points > contests[contest][user]:
                users[user] -= contests[contest][user]
                users[user] += points

                contests[contest][user] = points

for cont, participants in contests.items():
    print(f"{cont}: {len(contests[cont])} participants")
    i = 1
    for k, v in sorted(participants.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        print(f"{i}. {k} <::> {v}")
        i += 1

print("Individual standings")
t = 1
for (u, p) in sorted(users.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{t}. {u} -> {p}")
    t += 1
