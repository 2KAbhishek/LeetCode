class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        while len(stones) > 1:
            stones.sort()
            s1, s2 = stones[-1], stones[-2]
            if s1 == s2:
                stones.pop()
                stones.pop()
            else:
                s1 = abs(s1 - s2)
                stones.pop()
                stones[-1] = s1

        return stones[-1] if len(stones) else 0

