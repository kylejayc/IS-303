"""
Inputs:
- How many items?
- 


Processes:
- Calculate subtotals 
- Scan inventory
- Membership lookup
- Tax calculation

Outputs:
- Print receipt
"""

INVENTORY = {
    "apple":   {"price": 1.25, "stock": 50},
    "bread":   {"price": 3.49, "stock": 30},
    "milk":    {"price": 4.99, "stock": 20},
    "cheese":  {"price": 6.75, "stock": 15},
    "chips":   {"price": 3.99, "stock": 40},
    "soda":    {"price": 1.99, "stock": 60},
    "eggs":    {"price": 5.49, "stock": 25},
    "chicken": {"price": 8.99, "stock": 10},
}


MEMBERS = {
    "M001": {"name": "Sarah Johnson",  "discount": 0.10},
    "M002": {"name": "Mike Chen",      "discount": 0.15},
    "M003": {"name": "Emma Davis",     "discount": 0.05},
}


# ============================================================
# 1: CHECKOUT — Scan items and calculate subtotal
# ============================================================

def scan_items():
   items_in_cart = []
   item = input("Scan item (or 'done' to finish): ").lower().strip()
   while item != "done":
       if item in INVENTORY:
           items_in_cart.append(item)
           print(f"Added {item} to cart. Price: ${INVENTORY[item]['price']:.2f}")
       else:
           print(f"Item '{item}' not found in inventory.")
       item = input("Scan item (or 'done' to finish): ").lower().strip()
   return items_in_cart


def calculate_subtotal(items_in_cart):
   subtotal = 0
   for item in items_in_cart:
       subtotal += INVENTORY[item]["price"]
   print(f"Subtotal: ${subtotal:.2f}")
   return subtotal


# ============================================================
# 2: INVENTORY — Check and update stock levels
# ============================================================

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


# ============================================================
# 3: LOYALTY — Membership lookup and discounts
# ============================================================

def calculate_total(subtotal, member_id):
   member = MEMBERS.get(member_id)


   if member:
       discount_rate = member["discount"]
       print(f"Member found: {member['name']} ({discount_rate * 100}% discount applied)")
   else:
       discount_rate = 0.0
       print("Guest checkout: No membership discount applied.")


   discount_amount = subtotal * discount_rate
   final_total = subtotal - discount_amount


   return final_total, discount_amount

# ============================================================
# 4: RECEIPTS & TAX — Tax calculation and receipt
# ============================================================

def tax_calculation(subtotal):
   tax_rate = 0.0735
   return subtotal * tax_rate


def generate_receipt(items_in_cart, subtotal, member, discount, total):
   receipt = []
   divider = "----------------------------"
   customer_name = member["name"] if member else "Guest"


   receipt.append(divider)
   receipt.append(f"Receipt for {customer_name}")
   receipt.append(divider)


   for item in items_in_cart:
       price = INVENTORY[item]["price"]
       receipt.append(f"1 x {item.capitalize()} @ ${price:.2f}")


   tax = tax_calculation(subtotal - discount)
   receipt.append(divider)
   receipt.append(f"Subtotal: ${subtotal:.2f}")
   if member:
       receipt.append(f"Membership Discount: -${discount:.2f}")
   receipt.append(f"Tax: ${tax:.2f}")
   receipt.append(divider)
   receipt.append(f"Total: ${total + tax:.2f}")
   receipt.append(divider)


   return "\n".join(receipt)


# ============================================================
# MAIN — Wires everything together
# ============================================================

def main():
   # Step 1: Checkout
   items_in_cart = scan_items()
   if not items_in_cart:
       print("No items scanned. Exiting.")
       return
   subtotal = calculate_subtotal(items_in_cart)


   # Step 2: Update stock
   for item in items_in_cart:
       update_stock(item, 1)


   # Step 3: Loyalty / discount
   user_id = input("Enter Member ID (or press Enter for guest): ").strip().upper()
   final, savings = calculate_total(subtotal, user_id)
   member = MEMBERS.get(user_id)


   # Step 4: Print receipt
   receipt = generate_receipt(items_in_cart, subtotal, member, savings, final)
   print(receipt)


main()


# ============================================================
# MAIN — The CEO wires everything together
# (Do NOT edit until integration phase)
# ============================================================