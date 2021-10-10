# Input

binary = input("Enter an binary number : ")



# Functions

def return_hexa(result):
    if result == 1:
        hexa = "A"
    elif result == 2:
        hexa = "B"
    elif result == 3:
        hexa = "C"
    elif result == 4:
        hexa = "D"
    elif result == 5:
        hexa = "E"
    elif result == 6:
        hexa = "F"

    print(f"Héxa is {hexa}")
    # print("Décimal is ")
    print("Décimal is ", end='')
    return result




# Variables

a = 0
b = 1
c = 2
d = 3



# Execution

if len(binary) == 20 and binary.isnumeric():

    for i in range(5):

        result = (int(binary[a]) * (2 ** 3)) + (int(binary[b]) * (2 ** 2)) + (int(binary[c]) * (2 ** 1)) + (int(binary[d]) * (2 ** 0))

        i += 1

        a += 4
        b += 4
        c += 4
        d += 4


        if len(str(result)) == 1:
            print(return_hexa(result))
        elif len(str(result)) == 2:
            int_result = (tuple(int(c) for c in str(result)))
            decimal = int_result[0] + int_result[1]
            print(return_hexa(decimal))
else:
    print("Error ! Format is not valid")