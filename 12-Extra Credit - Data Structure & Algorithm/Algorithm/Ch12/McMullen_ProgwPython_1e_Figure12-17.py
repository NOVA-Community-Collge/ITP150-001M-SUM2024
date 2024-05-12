# Note that this program will not display anything, for source code correctness only.

#Recursion
def sum_numbers(current_number):
    if current_number == 0:
        return 0
    else:
        sum_total = sum_numbers(current_number - 1)
        return current_number + sum_total
sum_numbers(10)
#Tail Recursion
def sum_numbers(sum_total, current_number):
    if current_number == 0:
        return sum_total
    else:
        sum_total = sum_total + current_number
        return sum_numbers(sum_total, current_number - 1)
sum_numbers(0, 10)
