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

def image_calc():

    width = int_check(question="width: ", low=1)
    height = int_check(question="height: ", low=1)

    num_pixels = width * height
    num_bits = num_pixels * 24

    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
    f"\nNumber of bits {num_pixels} x 24 ={num_bits}")

    return answer

image_ans = image_calc()
print(image_ans)