cream_amount = 0
ice_amount = 0

# Functions
def make_ice_cream():
    global cream_amount
    global ice_amount
    
    if cream_amount <= 0:
        raise RuntimeError("Not enough cream to make ice cream.")
    elif ice_amount <= 0:
        raise RuntimeError("Not enough ice to make ice cream.")
    
    cream_amount -= 1
    ice_amount -= 1
    print("Ice cream was made!")

def add_cream(amount):
    if amount < 0:
        raise ValueError("Cannot add negative amounts of cream.")
    global cream_amount
    cream_amount += amount
    print("Thanks for the", amount, "cups of cream!")
   
def add_ice(amount):
    if amount < 0:
        raise ValueError("Cannot add negative amounts of ice.")
    global ice_amount
    ice_amount += amount
    print("Thanks for the", amount, "cups of ice!")
    
    
# Main program
choice = -1
amount = 0
print("Welcome to the Fantasy Ice Cream Shop! What do you want to do?")
while choice != 0:
    print("   1: Make ice cream")
    print("   2: Add cream")
    print("   3: Add ice")
    print("   0: Quit")
    
    choice = int(input("> "))
      
    try:
        if choice == 1:
            make_ice_cream()
        elif choice == 2:
            amount = int(input("How much?> "))
            add_cream(amount)
        elif choice == 3:
            amount = int(input("How much?> "))
            add_ice(amount)
    except Exception as e:
        error_message = str(e)        
        print(error_message)
    print()
  