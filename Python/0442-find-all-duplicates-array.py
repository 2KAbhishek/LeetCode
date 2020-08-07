class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        out =[]
        counts = Counter(nums)
        for count in counts:
            if counts[count] > 1:
                out.append(count)
        return out