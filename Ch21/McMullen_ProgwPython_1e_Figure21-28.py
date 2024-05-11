def print_matrix(matrix, node_names):
    print("{:>10s}".format(" |"), end="")
    for column in range(len(matrix[0])):		
        print("{:>8s}".format(node_names[column] + " |"), end="")    
    print()    
    print("-" * (len(matrix) * 10))    
    
    for row in range(len(matrix)):
        print("{:>10s}".format(node_names[row] + " |"), end="")
        for column in range(len(matrix[row])):
            print("{:>8s}".format(str(matrix[row][column]) + " |"), end="")
        print()     
    print()
    
def floyds(matrix):
    for i in range(len(matrix)):
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if r != c and matrix[r][i] != 0 and matrix[i][c] != 0:
                    if matrix[r][c] == 0:
                        matrix[r][c] = matrix[r][i] + matrix[i][c]
                    else:
                        matrix[r][c] = min(matrix[r][c], matrix[r][i] + matrix[i][c])

if __name__ == '__main__':
    node_names = ["START", "A", "B", "C", "D", "E", "EXIT"]
    
    matrix = [[0, 2,0,11,7, 0, 0],
              [2, 0,3,5, 0, 0, 0],
              [0, 3,0,0, 0, 3, 0],
              [11,5,0,0, 0, 0, 0],
              [7, 0,0,0, 0, 12,0],
              [0, 0,3,0, 12,0, 8],
              [0, 0,0,0, 0, 8, 0]]
             
    print_matrix(matrix, node_names)
    
    floyds(matrix)
    
    print("\nFloyd's:")
    
    print_matrix(matrix, node_names)
