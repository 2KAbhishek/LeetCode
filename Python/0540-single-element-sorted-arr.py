class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # counts = Counter(nums)
        # n = 1
        # [(x, y)] = counts.most_common()[:-n-1:-1]
        # return x

        res = 0
        for i in nums:
            res ^= i

        return res

