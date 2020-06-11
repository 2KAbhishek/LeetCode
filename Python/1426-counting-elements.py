class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        for elem in arr:
            if elem + 1 in arr:
                count += 1

        return count

