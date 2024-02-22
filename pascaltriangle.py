def pascal(row,col):
#идем окошком два по предыдущей строке
    row = int(input())
    col = int(input())
    n = 6
    if col == 0 or row == col:
        return 1
    else:
        return pascal(row-1,col-1)+ pascal(row-1,col)

    dp=[]
    for row in range(n):
        currentRow = []
        for col in range(row):
            currentRow.append(pascal((row,col)))
        dp.append()
# допилить