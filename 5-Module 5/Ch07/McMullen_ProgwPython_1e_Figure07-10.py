total_weight = 0
reps = int(input("How many reps? "))
weight = int(input("What size weights are you using? "))
for i in range(reps):
    total_weight = total_weight + (weight * 2)
    print("Rep", i, total_weight, "lbs so far.")
print("Your total lift is:", total_weight, " lbs.")
