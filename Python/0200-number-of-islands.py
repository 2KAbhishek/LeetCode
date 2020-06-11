class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) < 1:
            return 0

        def dfs(r, c):
            # Bound Checking
            if r<0 or c<0 or r>rows-1 or c>cols-1 or grid[r][c]=='0': return

            # Switch 1s to 0s
            grid[r][c] = '0'

            # Find 1s vertically and horizontally
            dfs(r-1, c) 
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]

                if cell == '1':
                    count += 1
                    dfs(r, c)

        return count

