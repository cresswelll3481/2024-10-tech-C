#ask for file type

def get_filetype():

    while True:
        response = input("file type: ").lower()

        # check for i or exit code
        if response == "xxx" or response == "i":
            return response

        #interger check
        elif response in ['integer','int']:
            return "integer"
        #image
        elif response in ['image','photo','img','photo','p']:
            return "image"
        #text
        elif response in ['text','txt','t']:
            return "text"

        elif response in ['music','m','mp3']:
            return "please input an integer, image, or text"

        #no vaild response
        else:
            print("Please input a valid file type")

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

def integer_calc():

    integer = int_check(question="integer: ", low=0)

    raw_binary = bin(integer)

    binary = raw_binary[2:]
    num_bits = len(binary)

    answer = f"{integer} in binary is {binary}" \
             f"  we need {num_bits} bits to represent it"

    return answer

def calc_text_bits():
    pass
    # words go here
    response = input("enter text...")

    #bits calculater
    num_chars = len(response)
    num_bits = num_chars * 8

    # answer and response
    answer = (f'" your text has {num_chars} characters. ' \
             f"\nwe need to multiply {num_chars} by 8 bits to represent it correctly. "
              f"\n which is {num_bits} bits")

    return answer
# main here:

want_instructions = input("press <enter> to read the instructions or any key to continue.")

if want_instructions == "":
    print(
        '''
    instructions
    - input your file type
    - enter there required numbers
    -see your answer 
    ''')

print("program continues")

while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break


    if file_type == 'i':

# ask if interger of photo.
        want_image = input("Press <enter> for an integer ot any key for an image")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        image_ans = integer_calc()
        print(image_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)

