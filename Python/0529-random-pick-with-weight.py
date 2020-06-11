class Solution:

    def __init__(self, w: List[int]):
        self.pre_sum = []
        pre_sum = 0

        for weight in w:
            pre_sum += weight
            self.pre_sum.append(pre_sum)
        self.total_sum = pre_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()

        lo, hi = 0, len(self.pre_sum)
        while lo < hi:
            mid = lo + (hi - lo)//2
            if self.pre_sum[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

