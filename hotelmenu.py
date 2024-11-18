#Define the menu of restaurant
menu = {
    'Pizza': 120,
    'Burger': 50,
    'Coffee': 60,
    'Tea': 20,
    'French Fries': 80,
    'Salad': 100,
}

#Greet the customer
print("Welcome to SHrAvAnI Restaurant")
print("Pizza: Rs120\nBurger: Rs50\nCoffee: Rs60\nTea: Rs20\nFrench Fries: Rs80\nSalad: Rs100")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No)")

if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total}")