class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        totalShift = 0
        
        for shiftDir, shiftAmount in shift:
            if shiftDir:
                totalShift -= shiftAmount
            else:
                totalShift += shiftAmount

        totalShift %= len(s)

        s = s[totalShift:] + s[:totalShift]

        return s

