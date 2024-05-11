some_numbers = []
print("Enter numbers or -1 to quit:")
number = int(input())
while number != -1:
    some_numbers.append(number)
    number = int(input())
print(some_numbers)