# Import

import hashlib
import random



# Password parameters

# hash_we_have = "8a069869956a4e0cf7ac69f9c20e0d49"
# hash_we_have = "8b270711503c2cb2bb68b836e9cd06ab" 969881
hash_we_have = "f515fc52614cf73ec5203a5308ce33db"



# Functions

def find_hash(hash):

    wanted_mdp = [0, 0, 0, 0, 0, 0, 0, 0]
    counter = 0

    while hash != wanted_mdp:

        hash = hashlib.md5(hash.encode())
        hash_hexa = hash.hexdigest()

        wanted_mdp -= 1
        counter += 1

        print(wanted_mdp)
        print(hash_hexa)
        print(f"Le nombre de tentative est de {counter}")

        if hash == hash_hexa:

            print(f"Your password is : {wanted_mdp}")
            print(f"Your pass word hash is : {hash_hexa}")
            break

# Execution

print(find_hash(hash_we_have))

