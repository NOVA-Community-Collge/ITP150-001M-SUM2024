def add_one(number):
    print("Inside function, before addition:", number)
    number += 1
    print("Inside function, after addition:", number)
    
number = 5
print("Outside function, before function call:", number)
add_one(number)
print("Outside function, after function call:", number)