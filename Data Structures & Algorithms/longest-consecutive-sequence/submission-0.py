class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visit = set()
        res = 0
        for ele in nums:
            visit.add(ele)
        
        for i in range(len(nums)):
            if nums[i] - 1 not in visit:
                j = i
                lcs = 0
                seq = nums[j]
                while seq in visit:
                    lcs+=1
                    seq+=1
                res = max(res, lcs)
                
        return res

        