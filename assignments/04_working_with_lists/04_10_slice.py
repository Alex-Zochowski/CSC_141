pizza = ['Pepperoni', 'Deluxe', 'Hawaiian', 'Cheese', 'Veggie', 'Meat Lovers','Buffalo Chicken', 'Supreme', 'Margherita']
for p in pizza:
    print(f"I like {p} pizza.")
print("I really love pizza!")

print("The first three items in the list are:")
for p in pizza[:3]:
    print(f"- {p}")

print("Three items from the middle of the list are:")
for p in pizza[3:6]:
    print(f"- {p}")

print("The last three items in the list are:")
for p in pizza[6:9]:
    print(f"- {p}")