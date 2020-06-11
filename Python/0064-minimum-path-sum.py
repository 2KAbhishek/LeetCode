class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not len(grid): return 0

        minSum, rows, cols = grid, len(grid) ,len(grid[0])

        for i in range(rows):
            for j in range(cols):

                if i > 0 and j > 0:
                    minSum[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i > 0:
                    minSum[i][j] += grid[i-1][j]
                elif j > 0:
                    minSum[i][j] += grid[i][j-1]

        return minSum[rows-1][cols-1]

