class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goodPos = i = len(nums) -1

        while i >= 0:
            if i + nums[i] >= goodPos:
                goodPos = i
            i -= 1

        return goodPos == 0

