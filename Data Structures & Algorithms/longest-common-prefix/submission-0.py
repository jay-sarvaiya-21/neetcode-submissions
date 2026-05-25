class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
       
        for i in range(len(min(strs))):
            curr = strs[0][i]
            print(curr)
            for j in range(1,len(strs)):
                if curr != strs[j][i]:
                    return ans
            ans += curr
        return ans
                
            
            