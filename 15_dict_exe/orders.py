products = {}

while True:
    command = input().split()
    if 'buy' in command:
        break

    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product not in products:
        products[product] = {'pr': price, 'quant': quantity}
    else:
        products[product]['pr'] = price
        products[product]['quant'] += quantity

for k, v in products.items():
    print(f"{k} -> {v['pr']*v['quant']:.2f}")

