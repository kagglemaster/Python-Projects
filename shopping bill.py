cart = {}

while True:
    item = input("Enter the item: ")
    price = int(input("Enter the price: "))
    cart.update({item : price})
    ask = input("Press b for total amount or just press enter to continue......")

    if ask.lower() == 'b':
        print("Food Items\n")
        print("Item        Quantity")
        print("---------------------")
        for item, quantity in cart.items():
            print(f"{item.ljust(12)} {quantity}")
        total = sum(cart.values())
        print("-------------------")
        print("Total".ljust(12), total)
 
        break
    
    else:
        continue