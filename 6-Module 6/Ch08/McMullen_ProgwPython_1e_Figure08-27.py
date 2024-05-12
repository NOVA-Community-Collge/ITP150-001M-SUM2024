matrix = []
rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
for r in range(rows):
    matrix.append([])
    for c in range(columns):
        matrix[r].append(0)
print(matrix)
