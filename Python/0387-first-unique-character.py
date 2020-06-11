class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        counts = Counter(s)

        for count in counts:
            if counts[count] == 1:
                return s.index(count)

        return -1

