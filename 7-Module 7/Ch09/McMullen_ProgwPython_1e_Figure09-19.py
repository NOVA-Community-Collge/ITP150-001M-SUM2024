def add_one_to_first_number(number_list):
    print("Inside function, before addition:",
          number_list)
    number_list[0] += 1
    print("Inside function, after addition:",
          number_list)
    
number_list = [10,5,4,2,6]
print("Outside function, before function call:",
      number_list)
add_one_to_first_number(number_list)
print("Outside function, after function call:",
      number_list)