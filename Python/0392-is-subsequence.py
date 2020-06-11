class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, lenS, lenT = 0, 0, len(s), len(t)

        while i < lenS and j < lenT:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == lenS

