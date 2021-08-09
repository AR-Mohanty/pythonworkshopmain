
import random
word_list = ["anurag", "suraj", "dhruv", "shiv", "paritosh"]

choosen_word = random.choice(word_list)
display = []
print(choosen_word)

guess_input = input("guess the letter").lower()

for letter in choosen_word:
    display += "_"
print(display)