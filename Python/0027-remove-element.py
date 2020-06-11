class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while val in nums:
            # nums.remove(val)
        # return len(nums)
        
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        
        return count