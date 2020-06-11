class Solution(object):
    def judgeSquareSum(self, c):
        sqrt = math.isqrt(c)
        left, right = 0, sqrt
        while left <= right:
            sqrtSum = left * left + right * right 
            if sqrtSum < c:
                left += 1
            elif sqrtSum > c:
                right -= 1
            else:
                return True
        return False