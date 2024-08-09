def num_check(question):

    error = "please enter width more than 0\n"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

keep_going = ""
while keep_going == "":

    width = num_check("width: ")
    print(width)

    length = num_check("height: ")
    print(length)

    cost = num_check("cost per meter: ")
    print(cost)

    primerter = (length + width) * 2
    price = primerter * cost

    print()
    print(f"primerter: {primerter} meters")
    print(f"cost: ${price} per meter")

    keep_going = input("Press enter to contunue or press any other key to quit  ")
    print()

    print("thank you for using the area / primeter calculater")