class Solution:
    def mySqrt(self, x: int) -> int:
        n = x
        while n*n > x:
            n = (n + x/n) // 2
        return int(n)