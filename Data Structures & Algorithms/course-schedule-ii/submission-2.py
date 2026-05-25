class Solution:
    def findOrder(self, numCourses: int, preq:List[List[int]]) -> List[int]:

        res = []
        visit = set()
        completed = set()

        adj = {courses:[] for courses in range(numCourses)}

        for crs, pre in preq:
            adj[crs].append(pre)
        
        def dfs(crs):
            print(crs)

            if crs in visit:
                return False
            if crs in completed:
                return True
            visit.add(crs)    
                                    


            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            completed.add(crs)

            res.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        print("here")
        return res

        