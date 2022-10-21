import math

num_of_ppl = int(input())
ele_maks_capacity = int(input())

cap = math.ceil(num_of_ppl / ele_maks_capacity)
print(cap)