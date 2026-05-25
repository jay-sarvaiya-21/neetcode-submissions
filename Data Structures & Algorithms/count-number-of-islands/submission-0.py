class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        count = 0
        visit = set()
        def dfs(r,c,count):
            if r < 0 or c < 0 or r >= rows  or c >= cols  or (r,c) in visit or grid[r][c] == "0":
                return False
            visit.add((r,c))
            print(visit)
            
            dfs(r+1,c,count)  
            dfs(r-1,c,count) 
            dfs(r,c+1,count) 
            dfs(r,c-1,count)
                
            print(count)
            
            return True
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    if dfs(r,c,count):
                        count+=1
        return count
                

        