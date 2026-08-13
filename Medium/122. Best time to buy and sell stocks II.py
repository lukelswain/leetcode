class Solution:
    def maxProfit(self, prices:list[int]) -> int:
        buy = prices[0]
        total_profit = 0
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - buy)
            if prices[i] < prices[i-1]:
                buy = prices[i]
                total_profit += profit
                profit = 0
                continue
            if i == len(prices)-1:
                total_profit += profit
        return total_profit