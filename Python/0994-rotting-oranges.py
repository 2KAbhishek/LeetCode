class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def rottenOranges(timestamp):
            to_be_continued = False
            count = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == timestamp:
                        if i < rows-1 and grid[i+1][j] == 1:
                            count += 1
                            grid[i+1][j] = timestamp+1
                        if j < cols-1 and grid[i][j+1] == 1:
                            count += 1
                            grid[i][j+1] = timestamp+1
                        if i > 0 and grid[i-1][j] == 1:
                            count += 1
                            grid[i-1][j] = timestamp+1
                        if j > 0 and grid[i][j-1] == 1:
                            count += 1
                            grid[i][j-1] = timestamp+1
                        if count >= 1: to_be_continued = True
            return to_be_continued

        timestamp = 2
        while rottenOranges(timestamp):
            timestamp += 1

        for row in grid:
            if 1 in row: return -1

        return timestamp - 2

