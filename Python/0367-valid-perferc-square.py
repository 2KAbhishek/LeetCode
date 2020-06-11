class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = num

        while n*n > num:
            n = (n + num/n) // 2

        return n*n == num

