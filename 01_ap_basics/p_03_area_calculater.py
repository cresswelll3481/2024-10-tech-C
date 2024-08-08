def num_cheack(question):
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

for item in range(0, 2):
    width = num_cheack("width: ")
    print(width)


print()
def num_cheack(question):
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

for item in range(0, 2):
    height = num_cheack("height: ")
    print(height)