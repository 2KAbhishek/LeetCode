class Solution:
    def singleNumber(self, nums: List[int]) -> int:
##         cnt = Counter(nums)
#         cnt = {}
#         for num in nums:
#             if num in cnt:
#                cnt[item] += 1
#             else:
#                cnt[item] = 1
#         for num in cnt:
#             if cnt[num] == 1:
#                 return num
        return int((sum(set(nums)) *3 - sum(nums)) /2)
