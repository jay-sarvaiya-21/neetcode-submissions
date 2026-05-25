class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {courses:[] for courses in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        visit = set()
        comp = set()
        res = []
        def dfs(crs):
            nonlocal res
            if crs in visit:
                print("hERE2")
                return False
            if crs in comp:
                return True
            
            visit.add(crs)

            for pre in adj[crs]:
                if not dfs(pre):
                    print("hERE")
                    return False

            visit.remove(crs)
            comp.add(crs)
            res.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res