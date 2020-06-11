class Solution:
    def findComplement(self, num: int) -> int:
        for exp in range(1,32):
            cap = 2 ** exp - 1
            if num <= cap:
                return cap - num