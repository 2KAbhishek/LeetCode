class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = 0
        curLen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curLen = 0
                continue
            curLen += 1
            maxLen = max(maxLen, curLen)

        return maxLen
