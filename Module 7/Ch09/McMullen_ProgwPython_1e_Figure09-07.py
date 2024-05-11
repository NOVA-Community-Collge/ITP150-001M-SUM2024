def receipt(size, toppings, price):
    print("Your order:")
    print(str(size) + "-inch", toppings, "pizza.")
    print("Total ${:0.2f}".format(price))
    print("Enjoy Trivia night!")
 
topping = "Veggie"
receipt(12, topping, 12.99)
