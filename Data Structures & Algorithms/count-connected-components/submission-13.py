class DSU:

    def __init__(self,n):
        self.par = [num for num in range(n)]
        self.rank = [1] * n

    def find(self,n):
        res = n
        while res != self.par[res]:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]
        return res

    def union(self,n1,n2):
        self.p1 = self.find(n1)
        self.p2 = self.find(n2)

        if self.p1 == self.p2:
            return False
        if self.rank[self.p1] > self.rank[self.p2]:
            self.par[self.p2] =  self.p1
            self.rank[self.p1] += 1
        else:
            self.par[self.p1] =  self.p2
            self.rank[self.p2] += 1
        return True




class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        dsu = DSU(n)
        for u,v in edges:
            if dsu.union(u,v):
                res -= 1
        return res

        