def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

size = int(input())

matrix = [[i + 1 for i in range(size)] for _ in range(size)]

print("матрица")
for row in matrix:
    print(row)
    
print("Транспонирование")
for row in transpose_matrix(matrix):
    print(row)
