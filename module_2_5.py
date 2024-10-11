def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return(matrix)
rezult_1 = get_matrix(2,2,10)
rezult_2 = get_matrix(3,5,42)
rezult_3 = get_matrix(4,2,13)
print(rezult_1)
print(rezult_2)
print(rezult_3)
