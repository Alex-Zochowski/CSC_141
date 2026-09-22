pizza = ['Pepperoni', 'Deluxe', 'Hawaiian']
friends_pizza = pizza[:]
for p in pizza:
    print(f"I like {p} pizza.")
print("I really love pizza!")

pizza.append('Cheese')
friends_pizza.append('Veggie')

print("\nMy favorite pizzas are:")
for p in pizza:
    print(f"{p}")

print("\nMy friend's favorite pizzas are:")
for p in friends_pizza:
    print(f"{p}")