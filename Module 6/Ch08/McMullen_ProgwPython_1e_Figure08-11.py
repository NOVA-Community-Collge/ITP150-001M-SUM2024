some_numbers = []
for i in range(5):
    number = int(input("Enter number " + str(i) + ": "))
    some_numbers.append(number)
print(some_numbers)

some_more_numbers = []
how_many = int(input("How many numbers do you want to enter? "))
for i in range(how_many):    
    number = int(input("Enter number " + str(i) + ": "))
    some_more_numbers.append(number)
print(some_more_numbers)