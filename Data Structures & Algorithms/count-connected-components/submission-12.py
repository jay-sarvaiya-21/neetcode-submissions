class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [ node for node in range(n)]
        rank = [1] * n
        comp = n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]  # Path compression
                res = par[res]
            return res

        def merge(n1,n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = par[p1]
                rank[p1] += 1
            else:
                par[p1] = par[p2] 
                rank[p2] += 1
            return 1


        for n1,n2 in edges:
            comp-= merge(n1,n2)
        return comp

        