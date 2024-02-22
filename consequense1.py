def count_seq():
    n = input()
    if n ==0 or n == 1 or n == 2:
        return n
    dp = [1,2,4]
    for i in range(3,n):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
        return dp[n]
