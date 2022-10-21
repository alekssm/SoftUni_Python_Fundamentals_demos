n = int(input())

snowball_quality_current = 0
snowball_quality_max = 0
stats1 = 0
stats2 = 0
stats3 = 0

for n in range (1, n + 1):
    snowball_used_snow = int(input())
    snowball_used_time = int(input())
    snowball_built_quality = int(input())
    snowball_quality_current = round((snowball_used_snow / snowball_used_time) ** snowball_built_quality)
    if snowball_quality_current > snowball_quality_max:
        snowball_quality_max = snowball_quality_current
        stats1 = snowball_used_snow
        stats2 = snowball_used_time
        stats3 = snowball_built_quality

print(f"{stats1} : {stats2} = {snowball_quality_max} ({stats3})")