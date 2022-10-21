list_1 = input().split()
bake = {}
for ind in range (0, len(list_1), 2):
    keys = list_1[ind]
    values = int(list_1[ind + 1])
    bake[keys] = values

print(bake)