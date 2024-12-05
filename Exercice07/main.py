def square(number):


    try:
        number = float(number)
    except ValueError:
        print ("Le paramètre doit être un nombre !")
        return (None)

    square = number*number

    return (square)


if __name__ == '__main__':

    number = input("Entrez un nombre: ")

    square = square(number)

    if square:

        print(f"Le carré est : {square}")
