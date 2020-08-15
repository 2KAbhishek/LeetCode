class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = float('-inf')
        count = 0

        for i in sorted(intervals, key = lambda x: x[1]):
            if i[0] >= end:
                end = i[1]
            else:
                count += 1

        return count
