# password generator
# 3 characters ,2 digits, 2symbols
import random
import array

# maximum length of password needed
# this can be changed to suit your password length
MAX_LEN = 8

# declare arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

num_letter = int(input("enter num of letter\n"))
num_symbol = int(input("enter num of symbol\n"))
num_numbers = int(input("enter num of number\n"))

# combines all the character arrays above to form one array
password = ""
for char in range(1,num_letter + 1):
    password += random.choice(LOCASE_CHARACTERS)

for char in range(1,num_symbol + 1):
    password += random.choice(SYMBOLS)

for char in range(2,num_letter + 1):
    password += random.choice(DIGITS)

print(password)