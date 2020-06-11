class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums) // 3
        counts = Counter(nums)
        out = []
        
        for count in counts:
            if counts[count] > majority:
                out.append(count)
        
        return out
    