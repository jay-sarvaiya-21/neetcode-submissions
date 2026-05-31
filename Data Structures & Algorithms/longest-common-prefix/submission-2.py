class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        for i in range(len(strs[0])):
            curr_ele = strs[0][i]
            print(curr_ele)
            for j in range(len(strs)):
                if i == len(strs[j]) or  curr_ele != strs[j][i]:
                    t = strs[j]
                    return t[:i]
            res += curr_ele
        return res
        
            
        