class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comp = 0
        d = {i:[] for i in range(n)}
        visit = set()
        comp = 0
        for e1,e2 in edges:
            d[e1].append(e2)
            d[e2].append(e1)

        print(d)

        def dfs(e):
            if e in visit:
                return
            visit.add(e)
            for edges in d[e]:
                dfs(edges)
            
            

        for i in range(n):
            if i not in visit:
                print(i)
                # visit.add(i)
                comp+=1
                dfs(i)
        # {0: [1], 1: [0, 2], 2: [1, 3], 3: [2], 4: [5], 5: [4]}
        return comp



        