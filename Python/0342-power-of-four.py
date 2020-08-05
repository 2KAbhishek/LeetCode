class Solution:
    def isPowerOfFour(self, n: int) -> bool:
#         power4 = []
#         for i in range(17):
#             power4.append(4 ** i)

#         return n in power4
        return n>0 and (n & n-1) == 0 and n & (0xAAAAAAAA) == 0
