print("Press 1 to connect to an account agent.")
print("Press 2 to troubleshoot your cable.")
print("Press 3 to troubleshoot your Internet.")
print("Press 0 to quit.")
choice = input()
if choice == "0":
    print("Bye.")
elif choice == "1":
    print("Transferring you to an account agent.")
elif choice == "2":
    print("Connecting you to a cable technician.")
elif choice == "3":
    print("Connecting you to an Internet specialist.")
else:
    print("Invalid input.")
