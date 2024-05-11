def get_pizza_price(pizza_type, medium_increase=2, large_increase=6):
    if pizza_type == "Cheese":
        small_price = 7.99
    elif pizza_type == "Veggie":
        small_price = 10.99
    else:
        small_price = 12.99
    
    medium_price = small_price + medium_increase
    large_price = small_price + large_increase
    
    return small_price, medium_price, large_price

small, medium, large = get_pizza_price("Veggie")
print("Small:  ${:.2f}".format(small))
print("Medium: ${:.2f}".format(medium))
print("Large:  ${:.2f}".format(large))

small, medium, large = get_pizza_price("Veggie", 1, 2)
print("On Sale! Discount!")
print("Small:  ${:.2f}".format(small))
print("Medium: ${:.2f}".format(medium))
print("Large:  ${:.2f}".format(large))

