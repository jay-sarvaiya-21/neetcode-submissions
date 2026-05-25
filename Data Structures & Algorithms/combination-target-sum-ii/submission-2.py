class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        
        def dfs(cur,total,i):
            if total == target:
                res.add(tuple(cur))
                return
            if i == len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(cur,total+candidates[i],i+1)
            cur.pop()
            dfs(cur,total,i+1)
        dfs([],0,0)
        return [list(s) for s in res]
        