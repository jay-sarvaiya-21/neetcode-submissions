class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        visit = set()
        def dfs(r,c):
            print(r,c)
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r,c))
            a = 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            # print(a)
            return a
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = max(area,dfs(r,c))
                    print(area)
        return area

        