print("Welcome to Python Cafe\n")
print("What would you like to have?")
print("---------------------------------------")
print("Items".ljust(18), "Price")
print("---------------------------------------")
menu = {"Salad" : 230,
        "Soft Drink" : 90,
        "Mini Pizza" : 500,
        "Club Sandwich" : 350,
        "Coffee" : 130,
        "Tea" : 80,
        "Water" : 60}

for item,price in menu.items():
    print(f"{item.ljust(18)} ${price}")

order = []
while True:
    item = input("Enter the item you want to order: ").title()
    if item in menu:
        order.append(item)
        while True:
            reorder = input("Do you want add another item? (yes/no) ")
            if reorder.lower() == "yes":
                order2 = input("Enter the item you want to order: ").title()
                if order2 in menu:
                    order.append(order2)
                else:
                    print("Invalid item")
            elif reorder.lower() == "no":
                print("---------------------------------------")
                print(f"Your order summary: {','.join(order)}")
                break
        break
            
    else:
        print("Invalid item")

total = 0
for i in range(len(order)):
    pay = menu[order[i]]
    total += pay
print(f"Your total bill is ${total}")
print("Thank you for ordering")

with open("sales.txt", "a") as f:
    for i in order:
        f.write(f"{i.ljust(18)} {menu[i]}\n")


   

 