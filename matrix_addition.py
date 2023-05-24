matrixA = [[1, 2, 13],
           [4, 5, 6],
           [7, 8, 9]]
matrixB = [[1, 2, 3],
           [4, 5, 6],
           [7, 14, 18]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(matrixA)):
    for j in range(len(matrixA[0])):
        result[i][j] = matrixA[i][j]+matrixB[i][j]


for k in result:
    print(k)

