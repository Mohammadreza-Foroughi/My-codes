'''First Solution'''
import random

while True:
    try:
        user_input = int(input('Enter password length: '))
        if user_input > 0:
            break
        print("Length must be greater than 0.")
    except ValueError:
        print('Enter only numbers: ')
    
chars_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
chars_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
num = [chr(i) for i in range(ord('0'), ord('9') + 1)]
chars_spe = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '?', '+', '/', '_', ':', '{', '}', '|', '<', '>', '-']

ls = []

while True:
    uppercsae_letter = input('Include uppercase letters? (y/n)').lower()
    if uppercsae_letter == 'y':
        ls += (chars_upper)
        break
    elif uppercsae_letter == 'n':
        break
    else:
        print('invalid input')

while True:
    lower_letter = input('Include lower letters? (y/n)').lower()
    if lower_letter == 'y':
        ls += (chars_lower)
        break
    elif lower_letter == 'n':
        break
    else:
        print('invalid input')

while True:
    number = input('Include number? (y/n)').lower()
    if number == 'y':
        ls += (num)
        break
    elif number == 'n':
        break
    else:
        print('invalid input')

while True:
    special = input('Include special characters? (y/n)').lower()
    if special == 'y':
        ls += (chars_spe)
        break
    elif special == 'n':
        break
    else:
        print('invalid input')



if not ls:
    print('No character types selected — cannot generate password.')
else:
    result = ''.join(random.choice(ls) for _ in range(user_input))
    print(result)

'''Second Solution The better version for password'''


import secrets, string

while True:
    try:
        length = int(input('Enter password length: (second) '))
        if length > 0 :
            break
        print('Length must be greater than 0.')
    except ValueError:
        print('Enter only numbers: ')

pool = ''


while True:
    uppercsae_letter_2 = input('Include uppercase letters? (y/n)').lower()
    if uppercsae_letter_2 == 'y':
        pool += (string.ascii_uppercase)
        break
    elif uppercsae_letter_2 == 'n':
        break
    else:
        print('invalid input')

while True:
    lower_letter_2 = input('Include lower letters? (y/n)').lower()
    if lower_letter_2 == 'y':
        pool += (string.ascii_lowercase)
        break
    elif lower_letter_2 == 'n':
        break
    else:
        print('invalid input')

while True:
    number_2 = input('Include number? (y/n)').lower()
    if number_2 == 'y':
        pool += (string.digits)
        break
    elif number_2 == 'n':
        break
    else:
        print('invalid input')

while True:
    special_2 = input('Include special characters? (y/n)').lower()
    if special_2 == 'y':
        pool += (string.punctuation)
        break
    elif special_2 == 'n':
        break
    else:
        print('invalid input')



if not pool:
    print('No character types selected — cannot generate password.')
else:
    result = ''.join(secrets.choice(pool) for _ in range(length))
    print(result)
