# checks users enter a number that is more than zero
def factor_check(question):

    error = "please enter an integer more that is between 1 and 200 inclusive\n"

    # loop until a valid number is entered
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:

            response = int(response)

            if 1 <= response <= 200:
                return response
            else:
                print(error)

        # if the user doesn't enter a number, output the error
        except ValueError:
            print(error)


#  main
while True:
    to_factor = factor_check("to factor: ")
    print("you chose to factor", to_factor)

    if to_factor == "xxx":
        break

