class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {courses:[] for courses in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit:
                print("hERE2")
                return False
            if adj[crs] == []:
                return True
            
            visit.add(crs)

            for pre in adj[crs]:
                if not dfs(pre):
                    print("hERE")
                    return False

            visit.remove(crs)
            adj[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
        

        