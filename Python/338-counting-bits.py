class Solution:
    def countBits(self, num: int) -> List[int]:
#         return [Counter(bin(i))['1'] for i in range (0,num+1)]

#       len(res) doubles every time
        res = [0]
        while len(res) <= num:
            res += [i+1 for i in res]
        return res[:num+1]

#       uses [i-1]th elements count to get ith count           
#         dp = [0] * (num + 1)        
#         for i in range (1, num + 1):
#             dp[i] = dp[i & (i-1)] + 1
#         return dp
        