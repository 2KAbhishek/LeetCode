class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        cheapest = sys.maxsize
        
        for price in prices:
            if price < cheapest:
                cheapest = price
            else:
                profit = max(profit, price - cheapest)
        
        return profit