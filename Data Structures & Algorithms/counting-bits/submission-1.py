class Solution:
    def countBits(self, n: int) -> List[int]:

        def count(n):
            res = 0
            while n:
                res+= n % 2 
                n = n // 2
            return res

        res = []
        for i in range(n + 1):
            res.append(count(i))
        return res
        

        