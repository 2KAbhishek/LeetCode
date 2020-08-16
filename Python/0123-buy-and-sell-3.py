class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        b1, s1, b2, s2 = float('inf'), 0, float('inf'), 0

        for price in prices:
            b1 = min(b1, price)
            s1 = max(s1, price - b1)
            b2 = min(b2, price - s1)
            s2 = max(s2, price - b2)

        return s2
