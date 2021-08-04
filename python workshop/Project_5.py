pizza_size = input("Press L for large pizza\n M for medium\n S for small size of pizza ").upper()
pizza_toppings = input("Topping needed Y for yes and N for no ").upper()
pizza_extracheez = input("Need extra cheese y for yes and N for no ").upper()
bill = 0
if pizza_size == 'L':
    bill = bill + 12
    if pizza_toppings == 'Y':
        bill = bill + 3
    else:
        print("toppings not added")
    if pizza_extracheez == 'Y':
        bill = bill + 1
    else:
        print("extracheez not added")
elif pizza_size == 'M':
    bill = bill + 7
    if pizza_toppings == 'Y':
        bill = bill + 3
    else:
        print("toppings not added")
    if pizza_extracheez == 'Y':
        bill = bill + 1
    else:
        print("extracheez not added")
elif pizza_size == 'S':
    bill = bill + 5
    if pizza_toppings == 'Y':
        bill = bill + 3
    else:
        print("toppings not added")
    if pizza_extracheez == 'Y':
        bill = bill + 1
    else:
        print("extracheez not added")
else:
    print("choose valid options")

print(f"bill is {bill} $")
