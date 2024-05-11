
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

def display_numbers(current_number):
    if current_number > 10:
        return
    else:
        print(current_number)
        display_numbers(current_number + 1)

display_numbers(1)