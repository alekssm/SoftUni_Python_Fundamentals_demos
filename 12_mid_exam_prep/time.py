import math

emp_1_efficiency = int(input())
emp_2_efficiency = int(input())
emp_3_efficiency = int(input())
people = int(input())

ppl_per_hour = emp_1_efficiency + emp_2_efficiency + emp_3_efficiency
hours = 0
while people > 0:
    people -= ppl_per_hour
    hours += 1
    if hours % 4 == 0:
        hours +=1
print(f"Time needed: {hours}h.")