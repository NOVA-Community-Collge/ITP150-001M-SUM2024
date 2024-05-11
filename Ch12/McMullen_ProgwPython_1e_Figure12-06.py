def guess_number(low, high):
    # Comments are indicated with a # at the beginning.
    
    # Base case
    if low > high:
        return -1
    
    middle = (low + high) // 2   
    hint = input("Is your number " + str(middle) + "? ")
    
    # Base case
    if hint == "correct":
        return middle
    # higher
    elif hint == "higher":
        return guess_number(middle + 1, high)
    # lower
    else:
        return guess_number(low, middle - 1)


print("Enter higher, lower, or correct.")
print("Think of a number between 1 and 10!")
number = guess_number(1, 10)
if number != -1:
    print("Your number is " + str(number) + "!")
else:
    print("You cheated :(")
    



