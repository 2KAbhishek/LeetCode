class Solution:
    def climbStairs(self, n: int) -> int:
        # a = b = 1
        # for _ in range(n):
        #     a, b = b, a + b
        # return a

        memo = {}
        memo[0] = 1
        memo[1] = 1

        for k in range(2,n+1):
            f = memo[k-1] + memo[k-2]
            memo[k] = f

        return memo[n]

