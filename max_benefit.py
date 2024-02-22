def maxProfit(prices):
    prices = [int(i) for i in input().split()]
    profit = 0
    min_price = int(prices[0])
    for curPrice in range(len(prices)):
        # if i > profit:
        #     profit = i - min_price
        # if i < min_price:
        #     min_price = i
        profit = max(profit, prices[curPrice] - min_price)
        min_price = min(prices[curPrice], min_price)
    return profit