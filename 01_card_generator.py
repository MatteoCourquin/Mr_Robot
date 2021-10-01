# Import

import random

# Variables

type_card = input("Entrez 'visa' ou 'mastercard' : ")

card = []

counter = 0

# Execution

if type_card == "visa" or type_card == "mastercard":

    if type_card == "visa":
        visa = card.append("4")

    elif type_card == "mastercard":
        mastercard= card.append("5")

    while len(card) < 16:

        counter += 1
        random_number = (random.randint(1, 9))

        card.append(random_number)

    print(f" Voici votre carte {type_card} : {''.join(map(str, card[0:4]))} {''.join(map(str, card[4:8]))} {''.join(map(str, card[8:12]))} {''.join(map(str, card[12:16]))}")

elif type_card != "mastercard" or type_card != 'visa':
    print("Le format de la carte n'est pas valide")

