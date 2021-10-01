# Import

import random
import string


# Variables

length_password = input('How long for your password? : ')

password = []

counter = 0


# Execution

if length_password.isnumeric():

    while len(password) < int(length_password):
        counter += 1
        random_number = (random.randint(1, 9))
        random_letter = string.ascii_letters
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        password.append(random_number)
        password.append(random.choice(random_letter))

    random.shuffle(password)
    print(f"Your password suggest is : {''.join(map(str, password))}")

else:
    print("Error ! Please enter a number.")
