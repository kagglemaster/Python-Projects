import random

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S','T','U', 'V', 'W', 'X', 'Y', 'Z',
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           ';', ',', '_', '=', '}', '{', '[', ']', '?', '\\', '/', '!', '#', '$', '%', '&', '(', ')', '*', '+']

length = int(input("Enter the length of password: "))

if length <= 20:
    for i in range(1, length+1):
        print(random.choice(chars), end="")
else:
    print("Max length is of 20 characters.")
