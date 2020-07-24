year = int(input("Enter a year for check it is a leap year or not? (For example 1980): "))

if year % 4 == 0 and year % 100 != 100 or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
