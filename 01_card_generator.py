# Import

import random

# Fonctions

card = []

type_card = input("Entrez 'visa' ou 'mastercard' : ")



counter = 0

while len(card) < 15:

    counter += 1
    random_number = (random.randint(1, 9))

    if type_card == "visa" or type_card == "VISA":
        card.append("4")
        card.append(random_number)

    elif type_card == "mastercard" or type_card == "MASTERCARD":
        card.append("5")
        card.append(random_number)

    elif type_card != "mastercard" or type_card != 'visa':
        print("Le format de la carte n'est pas valide")
        break


print(f" Voici votre carte {type_card} : {''.join(map(str, card[0:4]))} {''.join(map(str, card[4:8]))} {''.join(map(str, card[8:12]))} {''.join(map(str, card[12:16]))}")
