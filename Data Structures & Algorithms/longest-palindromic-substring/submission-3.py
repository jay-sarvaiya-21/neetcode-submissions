class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        for i in range(n):

            prev = i 
            nxt = i 
           
            while prev >= 0 and nxt < n and s[prev] == s[nxt]:
                
                if (nxt - prev + 1) > len(res):
                    res = s[prev:nxt+1]
                prev = prev -1
                nxt = nxt + 1


            prev = i 
            nxt = i + 1
           
            while prev >= 0 and nxt < n and s[prev] == s[nxt]:
                
                if (nxt - prev + 1) > len(res):
                    res = s[prev:nxt+1]
                prev = prev -1
                nxt = nxt + 1
            
        return res if res else s[0]
