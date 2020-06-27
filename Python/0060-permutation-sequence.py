class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1,n+1))
        res = ""
        k -= 1   # since index starts from 0
        while n > 0:
            n -= 1
            idx, k = divmod(k, math.factorial(n))
            res += str(nums[idx])
            nums.pop(idx)

        return res
