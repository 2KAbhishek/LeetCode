class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k = 0, 2
        for n in nums:
            if i < k or n > nums[i-k]:
                nums[i] = n
                i += 1
        return i