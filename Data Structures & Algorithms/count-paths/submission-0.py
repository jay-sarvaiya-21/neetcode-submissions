class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        rows = m
        cols = n
        visit = set()
        count = 0 
        def dfs(r,c):
            nonlocal count
            if r >= rows or c >= cols:
                return 0

            if r == m - 1 and c == n - 1:
                count += 1
            
            dfs(r+1,c) 
            dfs(r,c+1)
        dfs(0,0)
        return count