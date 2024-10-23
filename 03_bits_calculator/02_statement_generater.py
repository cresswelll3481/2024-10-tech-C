# functions go under

def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("instructions", "*")
    print('''
Instructions go here.
- bake cake
- eat cake 
- wish you had more cake
        ''')


# Main rouitne goes here
want_instructions = input("press <enter> to read the instructions or any key to continue.")

want_instructions == "":
    instructions()

print("program continues")
