ld = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    ld[1] = 29
day += 1
if day > ld[month - 1]:
    day = 1
    month += 1
    if month > 12:
        month = 1
        year += 1
print(f"Day: {day} Month: {month} Year: {year}")
if (day== 28 and month == 3):
    print("Happy Birthday Nadeen")