# Import

import hashlib


# Variables

hash_we_have = "8a069869956a4e0cf7ac69f9c20e0d49"
# 72047838



# Functions

def find_hash(hash_we_have):

    str2hash = 99999999

    # str2hash = 73047838 (fonction de test pour soulager nos ordis ;) )

    while hash_we_have != str2hash:

        hash = hashlib.md5(str(str2hash).encode())

        print(hash.hexdigest())
        print(str2hash)

        if hash.hexdigest() == hash_we_have:
            print(f"Your password is {str2hash}")
            print(f"Your password hash is : {hash.hexdigest()}")
            break
        elif str2hash == 9999999:
            print("No matches with your hash password's were found")
            break

        str2hash -= 1



# Execution

print(find_hash(hash_we_have))