print("Welcome to rollercoster")
height = int(input("What is your height in cm?"))

total_charge = 0
if height > 120:
    print("You could ride rollercoster")
    age = int(input("What is your age?"))
    if age <= 12:
        print("Child tickets are $2")
        total_charge += 2
    elif age <= 18:
        print("Youth tickets are $4")
        total_charge += 4
    elif age <= 60:
        print("Adult ticket are $7")
        total_charge += 7
    else:
        print("Senior citizen can ride free")
    want_photo = input("Do you want photo? Y/N").upper()
    if want_photo == 'Y':
        total_charge += 3
        print(f"Your total bill is {total_charge}")
else:
    print("Sorry you cannot ride because your height is too small")