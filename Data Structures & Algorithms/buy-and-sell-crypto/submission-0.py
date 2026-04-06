class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, profit = prices[0], 0
        for i in range(len(prices)):
            if prices[i] - minimum > profit:
                profit = prices[i] - minimum
            if prices[i] < minimum:
                minimum = prices[i]
        return profit

