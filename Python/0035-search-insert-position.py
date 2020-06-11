class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        else:
            # nums.append(target)
            # nums.sort()
            # return nums.index(target)
            if target<min(nums):
                return 0
            elif target>max(nums):
                return len(nums)
            else:
                for i in range(len(nums)-1):
                    if target in range(nums[i], nums[i+1]):
                        return i+1

