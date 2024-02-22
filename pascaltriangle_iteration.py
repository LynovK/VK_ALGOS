def pascal(row,col):
    n = 6
    row = int(input())
    col = int(input())
    dp = []
    for i in range(1,n):
        tmp = []
        for j in range(1,i):
            tmp.append(1)
        dp.append(tmp)

    for row in range(1,n):
        for col in range(1,row):
            dp[row]
#допилить



