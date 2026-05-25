class Solution:
    def canFinish(self, numCourses: int, preq: List[List[int]]) -> bool:

        adj = {crs:[]for crs in range(numCourses)}
        visit = set()
        for crs,pre in preq:
            adj[crs].append(pre)

        def dfs(crs):

            if crs in visit:
                return False
            visit.add(crs)
            
            for pre in adj[crs]:
                if not dfs(pre):  
                    return False
            visit.remove(crs)
            return True



        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        