class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def strHelp(start, end):
            if start < end:
                s[start], s[end] = s[end], s[start]
                strHelp(start + 1, end - 1)

        strHelp(0, len(s) - 1)

