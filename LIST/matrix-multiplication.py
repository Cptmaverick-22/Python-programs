r1 = int(input("Enter the no of rows of 1st matrix: "))
c1 = int(input("Enter the no of columns of 1st matrix: "))
r2 = int(input("Enter the rows of 2nd matrix: "))
c2 = int(input("Enter the no of columns of 2nd matrix: "))

if c1 != r2:
    print("Matrix multiplication is not possible...")
else:
    mat1 = []
    mat2 = []
    result = []

    print("Enter the elements of the 1st matrix: ")
    for i in range(r1):
        row_1st = []
        for j in range(c1):
            key = int(input("Enter the value: "))
            row_1st.append(key)
        mat1.append(row_1st)

    print("Enter the elements of the 2nd matrix: ")
    for i in range(r2):
        row_2nd = []
        for j in range(c2):
            key = int(input("Enter the value: "))
            row_2nd.append(key)
        mat2.append(row_2nd)

    for i in range(r1):
        row_result = []
        for j in range(c2):
            sum = 0
            for k in range(c1):
                sum += mat1[i][k] * mat2[k][j]
            row_result.append(sum)
        result.append(row_result)

    print("First matrix is: ")
    for i in range(r1):
        for j in range(c1):
            print(mat1[i][j], end=" ")
        print()

    print("Second matrix is: ")
    for i in range(r2):
        for j in range(c2):
            print(mat2[i][j], end=" ")
        print()

    print("Result of matrix multiplication:")
    for row in result:
        print(row)
