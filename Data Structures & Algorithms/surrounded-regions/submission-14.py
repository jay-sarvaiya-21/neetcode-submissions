class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows,cols = len(board),len(board[0])
        visit = set()
        visit3 = set()


        
        
        # O -> T
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit or board[r][c] == "X":
                return
            visit.add((r,c))
            board[r][c] = "T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return
        # mark T
        for r in range(rows):
            for c in range(cols):                
                if [r,c] in [[0,c],[rows-1,c],[r,0],[r,cols-1]] and board[r][c] == "O":
                    print(r,c)
                    dfs(r,c)
        print(board)
        
        print(board)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # **Step 3**: Convert 'T' -> 'O' (restore border-connected regions)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        print(board)
                
        