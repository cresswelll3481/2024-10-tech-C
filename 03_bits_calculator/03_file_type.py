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


# main here:
while True:
    file_type = get_filetype()

    
    if file_type == 'i':

# ask if interger of photo.
        want_image = input("Press <enter> for an integer ot any key for an image")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"You chose {file_type}")

    if file_type == "xxx":
        break