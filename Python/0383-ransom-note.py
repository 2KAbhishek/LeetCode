class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR = Counter(ransomNote)
        countM = Counter(magazine)

        for char in countR:
            if countR[char] > countM[char]:
                return False

        return True

