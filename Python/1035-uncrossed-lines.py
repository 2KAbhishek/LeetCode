class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        # Same as longest common substring #1143
        n,m=len(A),len(B)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if A[i]==B[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]


