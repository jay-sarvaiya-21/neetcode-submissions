class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        def dfs(sub,i,total):
            nonlocal res
            if sum(sub) == target:
                res.append(sub[:])
                return
            if sum(sub) > target:
                return
            if  i >= len(nums):
                return
            
            sub.append(nums[i])
            dfs(sub,i,total+nums[i])
            sub.pop()
            dfs(sub,i+1,total)




        

        dfs([],0,0)
        return res
        