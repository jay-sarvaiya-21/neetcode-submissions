class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        
        fresh = 0
        rows, cols = len(grid),len(grid[0])
        q = deque()
        visit = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        t = 0


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    visit.add((i,j))
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        def checkBound(r,c):
        
            nonlocal fresh
            if r < 0 or c < 0  or r >= rows or c >= cols or (r,c) in visit or grid[r][c] == 0:
                return
            visit.add((r,c))
            if grid[r][c] == 1:
                fresh-=1
                grid[r][c] = 2
                q.append((r,c))
            
        

        while fresh > 0 and q:
            for i in range(len(q)):
                r,c =q.popleft()

                for dr,dc in directions:
                    newr,newc = r + dr, c +dc
                    print("in fun",fresh)
                    checkBound(newr,newc)
            t+= 1
        return t if fresh == 0 else -1

        