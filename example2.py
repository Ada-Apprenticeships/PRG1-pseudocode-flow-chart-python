"""
Day 1, Example 2: Free Delivery Checker (sequence + selection)
 
Traces to check:
  order_total = 25, order_weight_kg = 12 gives a delivery charge of 9.99
  order_total = 45, order_weight_kg = 15 gives a delivery charge of 0.00
"""
 
FREE_DELIVERY_THRESHOLD = 40.00
STANDARD_DELIVERY_CHARGE = 4.99
HEAVY_DELIVERY_CHARGE = 9.99
HEAVY_WEIGHT_LIMIT = 10.0
 
order_total = float(input("Order total in £: "))
order_weight_kg = float(input("Order weight in kg: "))
 
if order_total >= FREE_DELIVERY_THRESHOLD:
    delivery_charge = 0.00
else:
    if order_weight_kg > HEAVY_WEIGHT_LIMIT:
        delivery_charge = HEAVY_DELIVERY_CHARGE
    else:
        delivery_charge = STANDARD_DELIVERY_CHARGE
 
total_to_pay = order_total + delivery_charge
 
print(f"Delivery charge: £{delivery_charge:.2f}")
print(f"Total to pay: £{total_to_pay:.2f}")