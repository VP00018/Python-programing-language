menu = {
        "pizza" : 3.00,
        "popcorn" : 4.01,
        "nachos" : 3.01,
        "fries" : 6.00,
        "chips" : 2.00,
        "cold drink" : 4.00,
        "soda" : 3.90,
        "limka" : 5.15
        }
cart = []
total = 0

print("--------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------- YOUR ORDER -------")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")