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
while keep_going =="":


    width = num_check("width: ")
    print(width)

    height = num_check("height: ")
    print(height)

    area = width * height
    primiter = (width * 2) + (height * 2)

    print()
    print(f"perimeter:  {primiter} units")
    print(f"area:  {area} square units")
    print()

    keep_going = input("Press enter to contunue or press any other key to quit")
    print()

    print("thank you for using the area / primeter calculater")