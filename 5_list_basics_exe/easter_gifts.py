list_of_gifts = input().split(" ")

no_money = False

while not no_money:
    comm = input().split(" ")
    if "OutOfStock" in comm:
        gift = comm[1]
        for index in range (len(list_of_gifts)):
            if list_of_gifts[index] == gift:
                list_of_gifts[index] = "None"
    if "Required" in comm:
        gift = comm[1]
        ind = int(comm[2])
        if ind < len(list_of_gifts):
            list_of_gifts[ind] = gift
    if "JustInCase" in comm:
        gift = comm[1]
        list_of_gifts[-1] = gift
    if "No" in comm:
        no_money = True

for ele in list_of_gifts:
    if ele == "None":
        list_of_gifts.remove(ele)

print(" ".join(list_of_gifts))