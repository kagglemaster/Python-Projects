class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price
    
    def buy(self, req_items, money):
        cost = req_items*self.item_price
        if req_items <= self.num_items and money >= cost:
            self.num_items -= req_items
            return money - cost
        
        elif req_items > self.num_items:
            raise ValueError("Not enough items in the machine.")
        
        elif money < cost:
            raise ValueError("Not enough coins")
        