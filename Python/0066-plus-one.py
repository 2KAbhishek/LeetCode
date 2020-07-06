class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0

        for digit in digits:
            num *= 10
            num += digit

        num += 1

        out = map(int,str(num))

        return out
