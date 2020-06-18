class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return None
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            if board[i][0] == "O":
                self.dfs(i,0,board)
            if board[i][n-1] == "O":
                self.dfs(i,n-1,board)
        for j in range(n):
            if board[0][j] == "O":
                self.dfs(0,j,board)
            if board[m-1][j] == "O":
                self.dfs(m-1,j,board)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] != "U":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"
    
    
    def dfs(self, i, j, board):
        m, n = len(board), len(board[0])
        if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
            board[i][j] = "U"
            self.dfs(i+1,j,board)
            self.dfs(i-1,j,board)
            self.dfs(i,j+1,board)
            self.dfs(i,j-1,board)