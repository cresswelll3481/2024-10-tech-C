# functions go under

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


# Main rouitne goes here
want_instructions = input("press <enter> to read the instructions or any key to continue.")

want_instructions == ""

instructions()

print("program continues")
