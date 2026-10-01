class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        l, i = 0, 0
        res = 0
        for char in s:
            while char in visit:
                visit.remove(s[l])
                l+= 1
                
            res = max(res,i-l+1)
            visit.add(char)
            i+= 1
        return res

        