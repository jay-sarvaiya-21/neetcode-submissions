class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        cycle = set()
        visit = set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in d[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True


        d = defaultdict(list)
        for c,p in prerequisites:
            d[c].append(p)
        print(d)
        for courses in range(numCourses):
            if not dfs(courses):
                return []
        return output
        