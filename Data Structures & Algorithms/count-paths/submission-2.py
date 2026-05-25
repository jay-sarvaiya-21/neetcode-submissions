class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        rows = m
        cols = n
        visit = set()
        memo = []
        for i in range(rows):
            memo.append([]) 
            for j in range(cols):
                memo[i].append(-1)
        print(memo)
      
        def dfs(r,c):
            if r >= rows or c >= cols:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if memo[r][c] != -1:
                return memo[r][c]
            
            memo[r][c] = dfs(r+1,c) + dfs(r,c+1)
            return memo[r][c]
        
        return dfs(0,0)