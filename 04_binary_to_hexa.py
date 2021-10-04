binary = input("Enter an binary number : ")


def return_hexa(decimal):
    if decimal == 1:
        hexa = "A"
    elif decimal == 2:
        hexa = "B"
    elif decimal == 3:
        hexa = "C"
    elif decimal == 4:
        hexa = "D"
    elif decimal == 5:
        hexa = "E"
    elif decimal == 6:
        hexa = "F"

    print(f"Héxa is {hexa}")
    print(f"Décimal is {result}")


result = ((int(binary[0])) * (2 ** 3)) + ((int(binary[1])) * (2 ** 2)) + ((int(binary[2])) * (2 ** 1)) + ((int(binary[3])) * (2 ** 0))


if len(str(result)) == 1:
    print(return_hexa(result))
elif len(str(result)) == 2:
    int_result = (tuple(int(c) for c in str(result)))
    decimal = int_result[0] + int_result[1]
    print(return_hexa(decimal))