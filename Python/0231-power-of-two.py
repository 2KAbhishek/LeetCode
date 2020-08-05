class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # i = 1
        # while i < n:
        #     i *= 2
        # return i == n
        return n>0 and (n & n-1) == 0