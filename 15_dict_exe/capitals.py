countries = input().split(", ")
capitals = input().split(", ")

dd = {countries[i]: capitals[i] for i in range(len(countries))}

for k, v in dd.items():
    print(f"{k} -> {v}")
