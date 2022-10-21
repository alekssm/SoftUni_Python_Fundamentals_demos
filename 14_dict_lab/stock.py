list_1 = input().split()
products = input().split()

dict_of_products = {}
for ind in range (0, len(list_1), 2):
    keys = list_1[ind]
    val = list_1[ind + 1]

    dict_of_products[keys] = val

for item in products:
    if item in dict_of_products:
        print(f"We have {dict_of_products[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")