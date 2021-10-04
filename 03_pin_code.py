# Import

import hashlib
import random



# Password parameters

# hash_we_have = "8a069869956a4e0cf7ac69f9c20e0d49" (Password 8 numbers)
hash_we_have = "5c53292c032b6cb8510041c54274e65f"



# Functions

def find_hash(hash):

    wanted_mdp = []

    while hash != wanted_mdp:
        generate_mdp(wanted_mdp)
        hash = hashlib.md5(''.join(map(str, wanted_mdp)).encode())
        hash_hexa = hash.hexdigest()
        print(''.join(map(str, wanted_mdp)))
        print(hash_hexa)

        if hash_hexa == hash_we_have:

            print(f"Your password is : {''.join(map(str, wanted_mdp))}")
            print(f"Your pass word hash is : {hash_hexa}")
            break

        wanted_mdp.clear()


def generate_mdp(random_mdp):
    for i in range(4):
        random_number = (random.randint(1, 9))
        random_mdp.append(random_number)



# Execution

print(find_hash(hash_we_have))
