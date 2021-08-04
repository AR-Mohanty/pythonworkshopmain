name1 = input("What is your first name ").lower()
name2 = input("What is your second name ").lower()

combined_name: str = name1+name2
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
dig_1 = t+r+u+e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
dig_2 = l+o+v+e

love_score = str(dig_1) + str(dig_2)
love_score_i = int(love_score)

if love_score_i <= 10 or love_score_i >= 90:
    print(f"your love score is {love_score_i},you go together like coke and mentos")
elif 40 <= love_score_i <= 50:
    print(f"your love score is{love_score_i},you are alright go together")
else:
    print(f'your score{love_score_i}')

