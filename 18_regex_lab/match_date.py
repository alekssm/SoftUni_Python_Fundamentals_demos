import re

reg = r"(?P<Day>\d{2})(?P<sep>[/\.-])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})"

text = input()

res = re.finditer(reg, text)
for date in res:
    current = date.groupdict()
    print(f"Day: {current['Day']}, Month: {current['month']}, Year: {current['year']}")
