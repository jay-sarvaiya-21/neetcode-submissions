class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        visit = set()
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)


        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for neighbors in adj[node]:
                dfs(neighbors)


        comp = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                comp+=1
        return comp

        


        