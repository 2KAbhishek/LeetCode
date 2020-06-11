# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        dims = binaryMatrix.dimensions()
        rows, cols = dims[0], dims[1]
        result =-1

        if rows == 0 or cols == 0:
            return result

        r , c = 0, cols-1

        while (r < rows and c >= 0):
            if binaryMatrix.get(r,c) == 1:
                result = c
                c -= 1
            else:
                r += 1

        return result

