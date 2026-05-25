class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0 
        r = 0
        res = 0
        countS = {}
        maxF = 0
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r],0)
            maxF= max(maxF, countS[s[r]])
            while (r-l +1) - maxF> k:
                countS[s[l]]-=1
                l+=1
            
            

            res = max(res,r-l + 1)
        return res
        