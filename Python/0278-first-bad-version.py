# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        begin, end = 1, n
        
        while begin < end:
            
            mid = begin + (end - begin) / 2
            
            if isBadVersion(mid):
                end = mid
            else:
                begin = mid + 1
                
        return int(begin)