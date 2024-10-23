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

def integer_calc():

    integer = int_check(question="integer: ", low=0)

    raw_binary = bin(integer)

    binary = raw_binary[2:]
    num_bits = len(binary)

    answer = f"{integer} in binary is {binary}" \
             f"  we need {num_bits} to represent it"

    return answer

image_ans = integer_calc()
print(image_ans)