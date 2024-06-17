#creat a maneu 
menu={
    'Pizza':100,
    'Burger':60,
    'Tea': 20,
    'Salad':50,
    'Coffee':55,
    'Pasta':75,
}
#greet
print("Welcome to our Restaurant")
print("Pizza: Rs100 \nBurger: Rs60\nTea: Rs20\nSalad: Rs50\nCoffee: Rs55\nPasta: Rs75")

order_total=0

item_1 =input("Enter your item that you want = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your order{item_1}has been added to your list")
else:
    print(f"ordered item {item_1} is not available in menu")
another_item=input("Do you want something else ? (Yes/No)")
if another_item == "Yes":
    item_2=input("Enter the name of item_2 =")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"item {item_2}has been added i your list")
    else:
        print(f"ordered item{item_2} is not avaialble in menu")
print(f"The Total Amount of items is Rs {order_total}")