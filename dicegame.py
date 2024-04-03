import random

print(f"""*************** Welcome {input("Enter your Name: ")} to Rolling Dice Game ***************""")

while True:
    input("Press Enter to roll the dice..... ")
    num = random.randint(1, 6)
    print(num)

    if num == 6:
        print("Congratulations! You win.")
        ask = input("Do you want to quit the game? (yes/no): ")
        if ask.lower() == "yes":
            print("Thank you for playing.")
            break
        else:
            continue

    else:
        print("Sorry you didn't roll 6.. Try Again!")
        ask2 = input("Do you want to try again. (yes/no): ")
        if ask2.lower() == "yes":
            continue
        else:
            print("Thank you for playing")
            break

    