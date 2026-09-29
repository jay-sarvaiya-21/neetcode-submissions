class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS,COLS = len(grid), len(grid[0])
        fresh = 0
        visit = set()
        count = 0
        def check(r,c):
            nonlocal visit
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] != 1:
                
                return False
            visit.add((r,c))
            return True
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh:
            QLEN = len(q)

            for i in range(QLEN):
                cr,cc = q.popleft()
                
                directions = [[1,0],[-1,0],[0,-1],[0,1]]
                for dr,dc in directions:
                    nr, nc = cr+dr, cc + dc
                    if check(nr,nc):
                        q.append((nr,nc))
                        fresh -=1
            count +=1
        return count if fresh == 0 else -1
        