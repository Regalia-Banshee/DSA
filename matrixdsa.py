def setzeroes(matrix):
    rows,cols=len(matrix),len(matrix[0])
    zero_rows,zero_columns=set(),set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                zero_rows.add(i)
                zero_columns.add(j)

    for row in zero_rows:
        matrix[row]=0*[rows]
    for cols in zero_rows:
        matrix[cols]=0*[cols]

matrix=[[1,2,3],[1,0,1],[2,3,4]]
setzeroes(matrix)
print(matrix)