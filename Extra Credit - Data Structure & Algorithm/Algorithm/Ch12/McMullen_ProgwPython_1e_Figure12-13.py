def sum_numbers(current_number):
    if current_number == 0:
        return 0
    else:
        sum_total = sum_numbers(current_number - 1)
        return current_number + sum_total
print(sum_numbers(10))
