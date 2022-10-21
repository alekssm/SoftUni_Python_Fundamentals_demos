def your_order_is(product, quantity):
    if product == "coffee":
        whole_products_price = 1.50 * quantity
        return whole_products_price
    elif product == "coke":
        whole_products_price = 1.40 * quantity
        return whole_products_price
    elif product == "water":
        whole_products_price = 1.00 * quantity
        return whole_products_price
    elif product == "snacks":
        whole_products_price = 2.00 * quantity
        return whole_products_price

order = input()
num_of_products = int(input())
total_price_order = your_order_is(order, num_of_products)
print(f"{total_price_order:.2f}")