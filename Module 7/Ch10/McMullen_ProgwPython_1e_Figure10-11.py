  
choice = -1
amount = 0
print("Welcome to the Fantasy Ice Cream Shop! What do you want to do?")
try:
    while choice != 0:
        print("   1: Make ice cream")
        print("   2: Add cream")
        print("   3: Add ice")
        print("   0: Quit")
        
        choice = int(input("> "))
          
        if choice == 1:
            make_ice_cream()
        elif choice == 2:
            amount = int(input("How much?> "))
            add_cream(amount)
        elif choice == 3:
            amount = int(input("How much?> "))
            add_ice(amount)
        print()
except:
    print("Something went wrong.")


