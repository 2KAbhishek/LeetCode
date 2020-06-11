class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if len(prices) <= 1:
            return profit
        
        for i in range(1, len(prices)):
            if (prices[i] > prices[i-1]):
                profit += (prices[i] - prices[i-1])
        
        return profit