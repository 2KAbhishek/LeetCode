class Solution:
    from itertools import permutations 
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(permutations(nums))