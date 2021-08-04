year = input("enter your for checking if it is leap year or not")
year_int = int(year)
if year_int % 4 == 0:
    if year_int % 100 == 0:
        if year_int % 400 == 0:
            print(f"Year {year} is leap year")
        else:
            print(f"year {year} is not leap")
    else:
        print(f"Year {year} is leap year")
else:
    print(f"year {year} is not leap year")
