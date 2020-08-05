class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        clean = ""

        for ch in s:
            if ch.isalnum():
                clean += ch.lower()

        return clean == clean[::-1]
