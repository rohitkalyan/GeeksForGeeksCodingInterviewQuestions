if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    for i in range(len(matrix)):
        if i%2 == 0:
            print(matrix[i])
        else:
            matrix[i].reverse()
            print(matrix[i])
