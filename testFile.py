import hashlib


hash_we_have = 720478358

hash = hashlib.md5(str(hash_we_have).encode())
print(hash.hexdigest())

def find_hash(hash_we_have):

    str2hash = 720478358

    while hash_we_have != str2hash:

        hash = hashlib.md5(str(str2hash).encode())

        print(hash.hexdigest())
        print(str2hash)

        if hash.hexdigest() == hash_we_have:
            print(f"Your password is : {hash.hexdigest()}")
            break
        elif str2hash == 10000000:
            print("No matches with your hash password's were found")
            break

        str2hash += 1


# print(find_hash(hash_we_have))