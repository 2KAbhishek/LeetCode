class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
#         counts = Counter(nums)

#         for count in counts:
#             if counts[count] > majority:
#                 return count
        nums.sort()
        return nums[majority]

