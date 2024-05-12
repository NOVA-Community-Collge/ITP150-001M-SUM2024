from linkedList import LinkedList

my_list = LinkedList()
my_list.prepend("Ma")
my_list.prepend("Ga")
my_list.prepend("Re")
my_list.prepend("Sa")

print(my_list)

if "Ga" in my_list:
    print("Ga is in the list!")
else:
    print("Ga is not in the list!")