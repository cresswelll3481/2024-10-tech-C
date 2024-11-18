# checks users enter a number that is more than zero
import math


def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("instructions", "-")
    print('''
Instructions go here.
- enter an interger between 1 to 200
- it will tell you the factors of the chosen interger
- it will tell you if its a...
    prime number or perfect square
        ''')


def num_check(question):
    error = "please enter an integer more that is between 1 and 200 inclusive\n"

    # loop until a valid number is entered
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:

            response = int(response)

            if 1 <= response:
                return response
            else:
                print(error)

        # if the user doesn't enter a number, output the error
        except ValueError:
            print(error)


def factor(var_to_factor):
    factors_list = []

    stop = math.sqrt(to_factor)
    stop = int(stop)

    for item in range(1, stop + 1):

        print(f"\nchecking {item}...")

        # check if it's a factor
        if to_factor % item == 0:
            # if it's a factor, add it to the list of factors
            factors_list.append(item)

            # // find the integer value for the 'partner' (eg: 1, 12)
            partner = to_factor // item

            # check if partner is in the list, if it is not, add it.
            if partner not in factors_list:
                factors_list.append(partner)

            print(f"item = {item}, partner = {partner}")

    factors_list.sort()
    return factors_list


# Main routine goes here
statement_generator("Factor Finder", "-")
want_instructions = input("\npress <enter> to read the instructions or any key to continue.")

if want_instructions == "":
    instructions()

#  main
while True:

    comment = ""

    to_factor = num_check("\nEnter a integer to factor or (xxx) to quit:    ")
    print("you chose to factor", to_factor)

    if to_factor == "xxx":
        print("thank you for using factors calculator")
        break

    elif to_factor != 1:
        all_factors = factor(to_factor)

    else:
        all_factors = ""
        comment = "One is unity   It only has one factor, itself"

    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number"

    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    print(all_factors)
    print(comment)
