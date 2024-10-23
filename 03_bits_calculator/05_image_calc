# checks users enter a number that is more than zero
def int_check(question, low):

    error = "please enter width more than 0\n"

    # loop until a valid number is entered
    while True:

        try:
            response = int(input(question))

            if response >= low:
                return response
            else:
                print(error)

        # if the user doesn't enter a number, output the error
        except ValueError:
            print(error)


# get width, loop for testing purposes
for item in range(0, 2):
    integer = int_check(question="integer: ", low=0)
    print(integer)


for item in range(0, 2):
    width = int_check(question="width: ", low=1)
    print(width)



print()

# get height, loop for testing purposes
for item in range(0, 2):
    height = int_check(question="height: ", low=1)
    print(height)

