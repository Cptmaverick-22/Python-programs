n = int(input("enter a number: "))
l = []
for i in range(n):
    row  = []
    for j in range(i+1):
        row.append(0)
    l.append(row)
for i in range(n):
    for j in range(i+1):
        if(j==0 or i==j):
            l[i][j] = 1
        else:
            l[i][j] = l[i-1][j-1] + l[i-1][j]
            