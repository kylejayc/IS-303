def check_stock(item, quantity):
   if item in INVENTORY:
       if INVENTORY[item]["stock"] >= quantity:
           return True
       else:
           print(f"Not enough {item}!")
           return False
   else:
       print(f"{item} not found!")
       return False


def update_stock(item, quantity):
   if item in INVENTORY:
       INVENTORY[item]["stock"] -= quantity
       return True
   return False
