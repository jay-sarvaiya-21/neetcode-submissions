class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        h = {}
        l = 0
        res = 0
        for r in range(len(s)):
            char = s[r]
            while char in h:
                del h[s[l]]
                l += 1


            if char not in h:
                h[char] = 1
                res = max(res,len(h))
        return res