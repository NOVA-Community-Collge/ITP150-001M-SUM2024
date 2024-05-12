reps = int(input("Enter the number of reps for this lifting exercise: "))
while reps < 1 or reps > 25:
    reps = int(input("Try again. Reps have to be in the range 1 to 25: "))
print("Okay, you want to do", reps, "reps.")
