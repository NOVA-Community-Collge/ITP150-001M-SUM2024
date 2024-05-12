doubled = []
for i in range(50):
    doubled.append(i * 2)
print("Manual doubled numbers:")
print(doubled)
print()

doubled_LC = [i * 2 for i in range(50)]
print("List comprehension doubled numbers:")
print(doubled_LC)
print()