total_weight = 0
weight = int(input("What size weights are you using? "))
sets = int(input("How many sets? "))
reps = int(input("How many reps per set? "))
for s in range(sets):
    print("Set:", s)
    for r in range(reps):
        total_weight = total_weight + (weight * 2)
        print("    Rep:", r, "Progress:", total_weight, "lbs.")

print("Your total lift is:", total_weight, "lbs.")
