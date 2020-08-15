class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        maxLen = 0

        for ch in counts:
            maxLen += counts[ch] // 2 * 2
            if maxLen % 2 == 0 and counts[ch] % 2 == 1:
                maxLen += 1

        return maxLen

