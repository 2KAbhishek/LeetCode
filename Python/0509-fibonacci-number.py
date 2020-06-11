class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        if N == 2:
            return 1
        
        curr = 0
        prev1 = 1
        prev2 = 1
        
        for i in range(3, N+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return curr