class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        for c in s:
            num *= 26
            num += ord(c) - 64

        return num

