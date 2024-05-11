def linear_search(contact_list, first_name, last_name):
    for contact_index in range(len(contact_list)):
        contact = contact_list[contact_index]
        if contact.first_name == first_name and contact.last_name == last_name:
            return contact_index    
    return -1

def binary_search(contact_list, lower_index, upper_index, target_contact):
    if lower_index <= upper_index:
        midpoint_index = (lower_index + upper_index) // 2
        
        print("Lower index:", lower_index)
        print("Upper index:", upper_index)
        print("Midpoint index:", midpoint_index)
    
        if contact_list[midpoint_index] == target_contact:
            return midpoint_index
        
        elif (contact_list[midpoint_index] > target_contact):
            return binary_search(contact_list, lower_index, midpoint_index - 1, target_contact)
        
        else:
            return binary_search(contact_list, midpoint_index + 1, upper_index, target_contact)
    
    return -1