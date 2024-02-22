# Дан массив не отсортированных чисел. Надо найти макс длину возрастающей
# последовательности и вернуть ее (Наибольшая возрастающая последовательность)
def findLIS(nums):
    nums = input()
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    dp = [1] * len(nums)
    for i in range(len(nums)):
        if dp[i-1] < dp[i]:
            dp[i] = dp[i-1] + 1
    return max(dp)