cream_amount = 0
ice_amount = 0

def make_ice_cream():
    global cream_amount
    global ice_amount
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