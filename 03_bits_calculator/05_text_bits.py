#calculate number of bits needed to repersent text in ascii
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


# Main routine
text_ans =calc_text_bits()
print(text_ans)