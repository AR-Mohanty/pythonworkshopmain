import random

# rand_int = random.randint(5, 100)
# print(rand_int)
#
# rand_float = random.random()
# print(rand_float)
#
# rand_float = 5*random.random()+5
# print(rand_float)

names_frnd = input("who are going for lunch\n")
names = names_frnd.split(",")
print(names)
random_choice = random.choice(names)
# bill_pay = names[random_choice]
print(f"{random_choice} is going to buy the food")
