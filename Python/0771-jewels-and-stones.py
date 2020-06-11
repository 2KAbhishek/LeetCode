class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewelCount = 0

        for jewel in J:
            jewelCount += S.count(jewel)

        return jewelCount

