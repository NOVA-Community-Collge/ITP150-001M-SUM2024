from linkedList import LinkedList
my_list = LinkedList()
my_list.append("Sa")
my_list.append("Re")
my_list.append("Ga")
print("The original list:")
print(my_list)

if "Sa" in my_list:
    print("Found Sa in the list!")
else:
    print("Did not find Sa in the list.")
print()
    
my_list.insert("Hi", 2);
print("The list after the insertion:")
print(my_list)
