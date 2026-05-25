class Solution:
    def countSubstrings(self, s: str) -> int:

        visit = set()
        n = len(s)
        count = 0
        for i in range(n):
            # Odd
            curr = i
            nxt = i
            while curr >= 0 and nxt < n and  s[curr] == s[nxt]:
                if (curr,nxt) not in visit:
                    count += 1
                curr -= 1
                nxt +=  1
            #Even
            curr = i
            nxt = i + 1 
            while curr >= 0 and nxt < n and  s[curr] == s[nxt]:
                if (curr,nxt) not in visit:
                    count += 1
                curr -= 1
                nxt +=  1
        return count

