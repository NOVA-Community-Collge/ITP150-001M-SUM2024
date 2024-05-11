print("Press 1 when you are ready to")
print("connect to an account agent.")
print("Press 0 to quit.")
choice = input()
if choice == "0":
    print("Are you sure you want to quit?")
    sure_thing = input()
    if sure_thing == "y":
        print("Okay, you're sure. Disconnecting.")
    else:
        print("Connecting you to the help desk.")
else:
	 print("You chose option 1.")
	 print("Connecting you now.")
