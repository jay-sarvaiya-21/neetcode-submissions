class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        for i in range(len(strs[0])):
            curr_ele = strs[0][i]
            for j in range(len(strs)):
                if i == len(strs[j]) or  curr_ele != strs[j][i]:
                    return strs[j][:i]
        return strs[0]
        
            
        