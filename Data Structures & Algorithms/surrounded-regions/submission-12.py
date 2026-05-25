class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows,cols = len(board),len(board[0])
        visit = set()
        visit3 = set()


        def dfs3(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit3 or board[r][c] == "X" :
                return
            visit3.add((r,c))
            board[r][c] = "O"
            dfs3(r+1,c)
            dfs3(r-1,c)
            dfs3(r,c+1)
            dfs3(r,c-1)
            return

        def dfs2(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "X":
                return
            board[r][c] = "X"
            dfs2(r+1,c)
            dfs2(r-1,c)
            dfs2(r,c+1)
            dfs2(r,c-1)
            return
        
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
        # Capture by turning O to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    dfs2(r,c)
        print(board)
        for r in range(rows):
            for c in range(cols):
                if [r,c] in [[0,c],[rows-1,c],[r,0],[r,cols-1]] and board[r][c] == "T":
                    dfs3(r,c)
        print(board)
                
        