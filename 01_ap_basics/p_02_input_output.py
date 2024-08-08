# user's name
username = input("Whats your name: ")
# user"s fav num
user_fav_num = int(input("Whats your favorite number: "))
# double, half, square fav num
double = user_fav_num * 2
halve = user_fav_num / 2
square = user_fav_num * user_fav_num

# greet user
print(f"hello {username}")

# output the results
print ("your number doubled is...")
print (double)

print ("your number halved is...")
print(halve)

print ("your number squared is")
print(square)