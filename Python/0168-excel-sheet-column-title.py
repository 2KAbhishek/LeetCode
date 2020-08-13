class Solution:
    def convertToTitle(self, n: int) -> str:
        title = ""
        while (n > 0):
            n -= 1
            title = chr(n % 26 + 65) + title
            n //= 26

        return title

