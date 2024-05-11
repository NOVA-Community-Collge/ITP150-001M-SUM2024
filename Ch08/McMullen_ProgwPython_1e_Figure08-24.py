result = []
for i in range(50):
    if i % 3 == 0:
        result.append(i * 3)
print("Manual tripling every third number:")
print(result)
print()

result_LC = [i * 3 for i in range(50) if i % 3 == 0]
print("List comprehension tripling every third number:")
print(result_LC)
print()