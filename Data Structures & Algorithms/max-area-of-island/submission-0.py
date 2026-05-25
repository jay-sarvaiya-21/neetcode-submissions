class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows,cols = len(grid), len(grid[0])
        visit = set()
        area = 0
        def dfs(r,c):
            
            if r < 0 or c < 0 or r >= rows  or c >= cols  or (r,c) in visit or grid[r][c] == 0:
                return 0
            grid[r][c] = "0"
            visit.add((r,c))
            
            a = 1
            a+= dfs(r+1,c)  
            a+= dfs(r-1,c) 
            a+= dfs(r,c+1) 
            a+= dfs(r,c-1)
            return a
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                   area =max(dfs(i,j),area)
        return area




        