clothes_and_prices = input()
budget = float(input())

list_of_items = clothes_and_prices.split("|")

budget_left = budget
profit = 0
sold_items_all = 0
list_of_sold = []

for ele in list_of_items:
    ele_list_current = ele.split("->")
    type_of_item = ele_list_current[0]
    price_of_item = float(ele_list_current[1])

    if "Clothes" in ele and price_of_item <= 50 and price_of_item <= budget_left:
        budget_left -= price_of_item
        sold_item_price = price_of_item + (price_of_item * 0.4)
        profit += price_of_item * 0.4
        sold_items_all += sold_item_price
        current_item_listed = "{0:.2f}".format(sold_item_price)
        #print(f"{sold_item_price:.2f}", end = " ")
        list_of_sold.append(current_item_listed)

    if "Shoes" in ele and price_of_item <= 35 and price_of_item <= budget_left:
        budget_left -= price_of_item
        sold_item_price = price_of_item + (price_of_item * 0.4)
        profit += price_of_item * 0.4
        sold_items_all += sold_item_price
        current_item_listed = "{0:.2f}".format(sold_item_price)
        #print(f"{sold_item_price:.2f}", end = " ")
        list_of_sold.append(current_item_listed)

    if "Accessories" in ele and price_of_item <= 20.50 and price_of_item <= budget_left:
        budget_left -= price_of_item
        sold_item_price = price_of_item + (price_of_item * 0.4)
        profit += price_of_item * 0.4
        sold_items_all += sold_item_price
        current_item_listed = "{0:.2f}".format(sold_item_price)
        #print(f"{sold_item_price:.2f}", end = " ")
        list_of_sold.append(current_item_listed)

items_being_sold = " ".join(list_of_sold)
print(items_being_sold)
print(f"Profit: {profit:.2f}")

if budget_left + sold_items_all >= 150:
    print("Hello, France!")
else:
    print("Time to go.")