import  random
all_numbers = []

for item in range(0, 5):

    mystery_num = random.randint(a=1, b=10)

    if mystery_num not in all_numbers:
        all_numbers.append(mystery_num)

all_numbers.sort()
print(all_numbers)