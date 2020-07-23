class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        out = []
        for num, count in counts.items():
            if count == 1:
                out.append(num)
        return out

