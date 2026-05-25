from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # if not board or not board[0]:
        #     return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "T"  # Temporarily mark the connected 'O' to border
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # **Step 1**: Mark border-connected 'O' cells as 'T'
        for r in range(rows):
            for c in range(cols):
                if [r,c] in [[0,c],[rows-1,c],[r,0],[r,cols-1]] and board[r][c] == "O":
                    dfs(r, c)
        
        # **Step 2**: Convert remaining 'O' -> 'X' (these are surrounded)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # **Step 3**: Convert 'T' -> 'O' (restore border-connected regions)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
