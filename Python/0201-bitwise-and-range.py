import math
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        top = int(math.log(n,2))
        bottom = int(math.log(m,2))
        if top != bottom:
            return 0

        res = m
        for i in range(m + 1, n + 1):
            res = res & i

        return res

