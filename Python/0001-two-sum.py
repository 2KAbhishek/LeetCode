class Solution:

    def twoSum(self, nums, target):
        
        num_indices = {}  # Maps nums[i] to i
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i
        return [-1, -1]
