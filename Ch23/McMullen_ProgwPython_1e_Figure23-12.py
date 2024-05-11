def binary_search(contact_list, lower_index, upper_index, target_contact):
    while lower_index <= upper_index:
        midpoint_index = (lower_index + upper_index) // 2
        
        print("Lower index:", lower_index)
        print("Upper index:", upper_index)
        print("Midpoint index:", midpoint_index)
    
        if contact_list[midpoint_index] == target_contact:
            return midpoint_index
        
        elif (contact_list[midpoint_index] > target_contact):
            upper_index = midpoint_index - 1
        
        else:
            lower_index = midpoint_index + 1
    
    return -1


### NOT INCLUDED IN FIGURE, FOR TESTING PURPOSES ###
if __name__ == '__main__':
    
    from phone_information import Contact    
    
    person1 = Contact("Amauhd", "McClain", "240-243-6532")
    person2 = Contact("Breonna", "Bland", "352-429-4372")
    person3 = Contact("Elijah", "Arbery", "313-809-6352")
    person4 = Contact("Floyd", "Garner", "734-546-6950")
    person5 = Contact("George", "Castile", "301-753-4543")
    person6 = Contact("Pamela", "Sterling", "864-754-3227")
    person7 = Contact("Riah", "Justice", "202-345-8643")
    person8 = Contact("Sandra", "Taylor", "443-567-6950")
    
    contact_list = [person1, person2, person3, person4,
                    person5, person6, person7, person8]
    
    found_index = binary_search(contact_list, 0, len(contact_list), person2)
    
    if found_index != -1:
        print("Breonna Bland is located at index:", found_index)
    else:
        print("Breonna Bland is not in the contact list.")