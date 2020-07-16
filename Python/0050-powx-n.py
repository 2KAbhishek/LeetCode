class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = abs(n)
        out = 1.00
        while m:
            if m & 1:
                out *= x
            x *= x
            m >>= 1
        return out if n >= 0 else 1/out

