weight = int(input("weight(kg)="))
height = float(input("height(m) = "))

bmi = weight / height ** 2
bmi = int(bmi)

print("Your bmi for weight", weight, "kg and height", height, "m is ..", bmi)
