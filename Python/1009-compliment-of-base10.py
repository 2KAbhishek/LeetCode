class Solution:
    def bitwiseComplement(self, N: int) -> int:
        for exp in range (1,32):
            cap = (2 ** exp) - 1
            if N <= cap:
                return cap - N

