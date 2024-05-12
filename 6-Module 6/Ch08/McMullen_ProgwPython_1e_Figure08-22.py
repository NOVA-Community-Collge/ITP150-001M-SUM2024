evens = []
for i in range(100):
    if i % 2 == 0:
        evens.append(i)
print("Manual even numbers:")
print(evens)
print()

evens_LC = [i for i in range(100) if i % 2 == 0]
print("List comprehension even numbers:")
print(evens_LC)
print()
