class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        out = []
        for n in num:
            while k and out and out[-1] > n:
                out.pop()
                k -= 1
            out.append(n)
        return ''.join(out[:-k or None]).lstrip('0') or '0'

