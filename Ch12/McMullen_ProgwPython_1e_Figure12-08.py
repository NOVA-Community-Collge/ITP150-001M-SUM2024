def add_numbers(current_number):
    if current_number > 10:
        return 0
    else:
        next_number = current_number + 1
        count = add_numbers(next_number)
        return current_number + count
print(add_numbers(1))
