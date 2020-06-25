class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numCounts = Counter(nums)
        [(num, times)] = numCounts.most_common(1)
        return num
