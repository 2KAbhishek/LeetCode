class Solution:
    def hIndex(self, citations: List[int]) -> int:
#         citations.sort(reverse=True)
#         for i in range(len(citations), 0, -1):
#             if citations[i - 1] >= i:
#                 return i
#         return 0
        n = len(citations)
        left, right = 0, n-1
        
        while left <= right:
            mid = (right + left) // 2
            if citations[mid] >= n-mid:
                right = mid - 1
            else:
                left = mid + 1
                
        return n - left