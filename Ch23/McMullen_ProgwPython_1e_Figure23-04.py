def linear_search(contact_list, first_name, last_name):
    for contact_index in range(len(contact_list)):
        contact = contact_list[contact_index]
        if contact.first_name == first_name and contact.last_name == last_name:
            return contact_index    
    return -1