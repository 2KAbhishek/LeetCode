from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result, sums = 0, 0
        rolling = defaultdict (lambda : 0)
        for num in nums:
            rolling[sums] += 1
            sums += num
            result += rolling[sums-k]
        return result

