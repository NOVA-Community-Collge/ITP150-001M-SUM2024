from phone_information import Contact
from search_algorithms import linear_search

person1 = Contact("Riah", "Justice", "202-345-8643")
person2 = Contact("George", "Castile", "301-753-4543")
person3 = Contact("Amauhd", "McClain", "240-243-6532")
person4 = Contact("Sandra", "Taylor", "443-567-6950")
person5 = Contact("Floyd", "Garner", "734-546-6950")
person6 = Contact("Elijah", "Arbery", "313-809-6352")
person7 = Contact("Pamela", "Sterling", "864-754-3227")
person8 = Contact("Breonna", "Bland", "352-429-4372")

contact_list = [person1, person2, person3, person4,
                person5, person6, person7, person8]

found_index = linear_search(contact_list, "Sandra", "Taylor")

if found_index != -1:
    print("Sandra Taylor is located at index:", found_index)
else:
    print("Sandra Taylor is not in the contact list.")